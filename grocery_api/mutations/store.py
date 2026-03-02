import graphene
from grocery_api.database import db_session
from grocery_api.models import Store
from grocery_api.types import StoreType


class CreateStore(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        opening_hours = graphene.String(required=True)

    store = graphene.Field(StoreType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, name, address, opening_hours):
        try:
            store = Store(
                name=name,
                address=address,
                opening_hours=opening_hours
            )
            db_session.add(store)
            db_session.commit()
            db_session.refresh(store)
            return CreateStore(store=store, success=True, message="Store created successfully")
        except Exception as e:
            db_session.rollback()
            return CreateStore(store=None, success=False, message=str(e))
