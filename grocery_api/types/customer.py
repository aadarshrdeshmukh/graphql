from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from grocery_api.models.customer import Customer


class CustomerType(SQLAlchemyObjectType):
    class Meta:
        model = Customer
        interfaces = (relay.Node,)
