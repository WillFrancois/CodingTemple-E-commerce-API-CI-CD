from flask import Blueprint
from controllers.Customer import create, list_all, customer_lifetime_value, update_customer, delete_customer, list_specific

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/add', methods=['POST'])(create)
customer_blueprint.route('/', methods=['GET'])(list_all)
customer_blueprint.route('/update', methods=['PUT'])(update_customer)
customer_blueprint.route('/delete', methods=['DELETE'])(delete_customer)
customer_blueprint.route('/find', methods=['GET'])(list_specific)
customer_blueprint.route('/customer_lifetime_value', methods=['GET'])(customer_lifetime_value)
