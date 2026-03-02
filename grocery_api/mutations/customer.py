import graphene
from grocery_api.database import db_session
from grocery_api.models import Customer
from grocery_api.types import CustomerType


class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        phone = graphene.String(required=True)

    customer = graphene.Field(CustomerType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, name, address, phone):
        try:
            customer = Customer(
                name=name,
                address=address,
                phone=phone
            )
            db_session.add(customer)
            db_session.commit()
            db_session.refresh(customer)
            return CreateCustomer(customer=customer, success=True, message="Customer created successfully")
        except Exception as e:
            db_session.rollback()
            return CreateCustomer(customer=None, success=False, message=str(e))
