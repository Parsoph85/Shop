from flask import Flask, request
from marshmallow import ValidationError

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.businsess_logic.product_usecases import product_get_by_id, product_get_many, product_create
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from eshop.view.product_schemas import ProductSchema, ProductGetManyParams, ProductCreateDtoSchema

app = Flask(__name__)


@app.post("/api/v1/order")
def order_create_endpoint():
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id_ord):
    order = order_get_by_id(id_ord)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)



@app.post("/api/v1/product")
def product_create_endpoint():
    try:
        prod_get = request.get_json(force=True)
        name = prod_get['name']
        price = prod_get['price']

    except ValidationError as err:
        return err.messages, 400

    try:
        product = product_create(name, price)

    except Exception as e:
        return {
            "error": str(e)
        }
    return ProductSchema().dump(product)



@app.get("/api/v1/product")
def product_get_many_endpoint():
    try:
        product_get_many_params = ProductGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    product = product_get_many(
        page=product_get_many_params['page'],
        limit=product_get_many_params['limit'],
    )
    return ProductSchema(many=True).dump(product)


@app.get("/api/v1/product/<id_prod>")
def product_get_by_id_endpoint(id_prod):
    product = product_get_by_id(id_prod)

    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return ProductSchema().dump(product)


def run_server():
    app.run()
