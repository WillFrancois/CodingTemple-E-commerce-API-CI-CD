from flask import request, jsonify
from models.schemas.CustomerAccountSchema import customer_account_schema, customers_accounts_schema
from services import CustomerAccount
from marshmallow import ValidationError
from utils.util import role_required

@role_required("admin")
def create():
    try:
        customer_account_data = customer_account_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    customer_account_save = CustomerAccount.create(customer_account_data)
    return customer_account_schema.jsonify(customer_account_save), 201

@role_required("admin")
def list_all():
    return customers_accounts_schema.jsonify(CustomerAccount.list_all())

@role_required("admin")
def update_customer_account():
    customer_account_id = request.args.get('id')
    try:
        customer_account_data = customer_account_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    return customer_account_schema.jsonify(CustomerAccount.update_customer_account(customer_account_data, customer_account_id))

@role_required("admin")
def delete_customer_account():
    customer_id = request.args.get('id')
    return CustomerAccount.delete_customer_account(customer_id)
