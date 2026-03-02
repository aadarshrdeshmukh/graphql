import graphene
from datetime import datetime, timedelta
from grocery_api.database import db_session
from grocery_api.models import Order, OrderItem, Customer, Store, Product, Inventory, OrderStatus
from grocery_api.types import OrderType, OrderStatusEnum


class OrderItemInput(graphene.InputObjectType):
    product_id = graphene.Int(required=True)
    quantity = graphene.Int(required=True)


class CreateOrder(graphene.Mutation):
    class Arguments:
        customer_id = graphene.Int(required=True)
        store_id = graphene.Int(required=True)
        items = graphene.List(graphene.NonNull(OrderItemInput), required=True)

    order = graphene.Field(OrderType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, customer_id, store_id, items):
        try:
            # Validate customer exists
            customer = db_session.query(Customer).filter(Customer.id == customer_id).first()
            if not customer:
                return CreateOrder(
                    order=None,
                    success=False,
                    message=f"Customer with id {customer_id} not found"
                )

            # Validate store exists
            store = db_session.query(Store).filter(Store.id == store_id).first()
            if not store:
                return CreateOrder(
                    order=None,
                    success=False,
                    message=f"Store with id {store_id} not found"
                )

            # Validate stock and collect order items data
            order_items_data = []
            total = 0.0

            for item in items:
                product = db_session.query(Product).filter(Product.id == item.product_id).first()
                if not product:
                    return CreateOrder(
                        order=None,
                        success=False,
                        message=f"Product with id {item.product_id} not found"
                    )

                # Check inventory
                inventory = db_session.query(Inventory).filter(
                    Inventory.store_id == store_id,
                    Inventory.product_id == item.product_id
                ).first()

                if not inventory or inventory.quantity < item.quantity:
                    available = inventory.quantity if inventory else 0
                    return CreateOrder(
                        order=None,
                        success=False,
                        message=f"Insufficient stock for {product.name}. Available: {available}, Requested: {item.quantity}"
                    )

                # Calculate item total
                item_total = product.price * item.quantity
                total += item_total

                order_items_data.append({
                    "product": product,
                    "quantity": item.quantity,
                    "price": product.price,
                    "inventory": inventory
                })

            # Create order
            delivery_time = datetime.now() + timedelta(hours=1)
            order = Order(
                customer_id=customer_id,
                store_id=store_id,
                status=OrderStatus.pending,
                total=total,
                delivery_time=delivery_time
            )
            db_session.add(order)
            db_session.flush()  # Get order ID

            # Create order items and deduct inventory
            for item_data in order_items_data:
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=item_data["product"].id,
                    quantity=item_data["quantity"],
                    price=item_data["price"]
                )
                db_session.add(order_item)

                # Deduct inventory
                item_data["inventory"].quantity -= item_data["quantity"]

            db_session.commit()
            db_session.refresh(order)
            return CreateOrder(order=order, success=True, message="Order created successfully")

        except Exception as e:
            db_session.rollback()
            return CreateOrder(order=None, success=False, message=str(e))


class UpdateOrderStatus(graphene.Mutation):
    class Arguments:
        order_id = graphene.Int(required=True)
        status = OrderStatusEnum(required=True)

    order = graphene.Field(OrderType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, order_id, status):
        try:
            order = db_session.query(Order).filter(Order.id == order_id).first()
            if not order:
                return UpdateOrderStatus(
                    order=None,
                    success=False,
                    message=f"Order with id {order_id} not found"
                )

            # Convert GraphQL enum to SQLAlchemy enum
            order.status = OrderStatus[status]
            db_session.commit()
            db_session.refresh(order)
            return UpdateOrderStatus(order=order, success=True, message="Order status updated successfully")

        except Exception as e:
            db_session.rollback()
            return UpdateOrderStatus(order=None, success=False, message=str(e))
