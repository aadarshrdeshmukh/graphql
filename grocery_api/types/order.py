import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from grocery_api.models.order import Order, OrderStatus as OrderStatusModel


class OrderStatusEnum(graphene.Enum):
    pending = "pending"
    preparing = "preparing"
    on_the_way = "on_the_way"
    delivered = "delivered"


class OrderType(SQLAlchemyObjectType):
    class Meta:
        model = Order
        interfaces = (relay.Node,)

    status = graphene.Field(OrderStatusEnum)

    def resolve_status(self, info):
        return self.status.value if isinstance(self.status, OrderStatusModel) else self.status
