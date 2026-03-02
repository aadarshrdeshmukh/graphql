import graphene
from grocery_api.database import db_session
from grocery_api.models import Product, Category, Inventory
from grocery_api.types import ProductType


class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        category_id = graphene.Int(required=True)
        price = graphene.Float(required=True)
        unit = graphene.String(required=True)

    product = graphene.Field(ProductType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, name, category_id, price, unit):
        try:
            # Validate category exists
            category = db_session.query(Category).filter(Category.id == category_id).first()
            if not category:
                return CreateProduct(
                    product=None,
                    success=False,
                    message=f"Category with id {category_id} not found"
                )

            product = Product(
                name=name,
                category_id=category_id,
                price=price,
                unit=unit
            )
            db_session.add(product)
            db_session.commit()
            db_session.refresh(product)
            return CreateProduct(product=product, success=True, message="Product created successfully")
        except Exception as e:
            db_session.rollback()
            return CreateProduct(product=None, success=False, message=str(e))
