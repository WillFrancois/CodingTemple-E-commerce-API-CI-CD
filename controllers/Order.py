from flask import request, jsonify
from models.schemas.OrderSchema import order_schema, orders_schema 
from services import Order
from marshmallow import ValidationError
from utils.util import role_required

@role_required("admin")
def create():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    order_save = Order.create(order_data)
    return order_schema.jsonify(order_save), 201

def list_all():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)
    return orders_schema.jsonify(Order.list_all(page, per_page))
