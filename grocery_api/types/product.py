import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from grocery_api.models.product import Product


class ProductType(SQLAlchemyObjectType):
    class Meta:
        model = Product
        interfaces = (relay.Node,)


class ProductWithStockType(graphene.ObjectType):
    """Product with stock information for a specific store"""
    product = graphene.Field(ProductType)
    in_stock = graphene.Int()
