import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from grocery_api.models.store import Store


class StoreType(SQLAlchemyObjectType):
    class Meta:
        model = Store
        interfaces = (relay.Node,)

    in_stock_products = graphene.List(lambda: graphene.NonNull("grocery_api.types.product.ProductWithStockType"))

    def resolve_in_stock_products(self, info):
        from grocery_api.types.product import ProductWithStockType
        products_with_stock = []
        for inv in self.inventory:
            if inv.quantity > 0:
                products_with_stock.append(ProductWithStockType(
                    product=inv.product,
                    in_stock=inv.quantity
                ))
        return products_with_stock
