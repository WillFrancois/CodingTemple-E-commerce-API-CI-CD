from flask import request, jsonify
from models.schemas.ProductSchema import product_schema, products_schema
from services import Product
from marshmallow import ValidationError
from utils.util import role_required

@role_required("admin")
def create():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    product_save = Product.create(product_data)
    return product_schema.jsonify(product_save), 201

def list_all():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)
    return products_schema.jsonify(Product.list_all(page, per_page))

def list_specific():
    product_id = request.args.get('id')
    return product_schema.jsonify(Product.list_specific(product_id))

def update_product():
    product_id = request.args.get('id')
    product_data = product_schema.load(request.json)
    return product_schema.jsonify(Product.update_product(product_data, product_id))

def delete_product():
    product_id = request.args.get('id')
    return jsonify(Product.delete_product(product_id))
