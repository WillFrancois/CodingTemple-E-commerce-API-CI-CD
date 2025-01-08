from flask import request, jsonify
from models.schemas.CustomerSchema import customer_schema, customers_schema
from services import Customer
from marshmallow import ValidationError
from utils.util import role_required

@role_required("admin")
def create():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    customer_save = Customer.create(customer_data)
    return customer_schema.jsonify(customer_save), 201

@role_required("admin")
def list_all():
    return customers_schema.jsonify(Customer.list_all())

@role_required("admin")
def list_specific():
    customer_id = request.args.get('id')
    return customer_schema.jsonify(Customer.list_specific(customer_id))

@role_required("admin")
def update_customer():
    customer_id = request.args.get('id')
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    return customer_schema.jsonify(Customer.update_customer(customer_data, customer_id))

@role_required("admin")
def delete_customer():
    customer_id = request.args.get('id')
    return Customer.delete_customer(customer_id)

@role_required("admin")
def customer_lifetime_value():
    return jsonify(Customer.customer_lifetime_value())
