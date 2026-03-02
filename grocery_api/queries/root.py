import graphene
from grocery_api.database import db_session
from grocery_api.models import Store, Customer, Order, Product, OrderStatus
from grocery_api.types import StoreType, CustomerType, OrderType, ProductType


class Query(graphene.ObjectType):
    store = graphene.Field(StoreType, id=graphene.Int(required=True))
    customer = graphene.Field(CustomerType, id=graphene.Int(required=True))
    orders = graphene.List(graphene.NonNull(OrderType), status=graphene.String())
    products_by_category = graphene.List(
        graphene.NonNull(ProductType),
        category_id=graphene.Int(required=True)
    )

    def resolve_store(self, info, id):
        return db_session.query(Store).filter(Store.id == id).first()

    def resolve_customer(self, info, id):
        return db_session.query(Customer).filter(Customer.id == id).first()

    def resolve_orders(self, info, status=None):
        query = db_session.query(Order)
        if status:
            try:
                status_enum = OrderStatus[status]
                query = query.filter(Order.status == status_enum)
            except KeyError:
                return []
        return query.all()

    def resolve_products_by_category(self, info, category_id):
        return db_session.query(Product).filter(Product.category_id == category_id).all()
