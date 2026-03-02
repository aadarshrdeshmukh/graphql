from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from grocery_api.models.order_item import OrderItem


class OrderItemType(SQLAlchemyObjectType):
    class Meta:
        model = OrderItem
        interfaces = (relay.Node,)
