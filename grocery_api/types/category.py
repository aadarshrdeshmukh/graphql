from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from grocery_api.models.category import Category


class CategoryType(SQLAlchemyObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node,)
