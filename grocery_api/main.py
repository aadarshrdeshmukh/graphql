from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler
import graphene
from grocery_api.database import init_db, db_session
from grocery_api.queries import Query
from grocery_api.mutations import (
    CreateStore,
    CreateProduct,
    CreateCustomer,
    CreateOrder,
    UpdateOrderStatus,
)


class Mutation(graphene.ObjectType):
    create_store = CreateStore.Field()
    create_product = CreateProduct.Field()
    create_customer = CreateCustomer.Field()
    create_order = CreateOrder.Field()
    update_order_status = UpdateOrderStatus.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

app = FastAPI(title="Grocery Delivery API")


@app.on_event("startup")
def startup_event():
    init_db()


@app.on_event("shutdown")
def shutdown_event():
    db_session.remove()


# GraphQL endpoint with Playground
app.mount(
    "/graphql",
    GraphQLApp(
        schema=schema,
        on_get=make_playground_handler()
    )
)


@app.get("/")
def read_root():
    return {
        "message": "Grocery Delivery GraphQL API",
        "graphql_endpoint": "/graphql",
        "playground": "/graphql (open in browser)"
    }
