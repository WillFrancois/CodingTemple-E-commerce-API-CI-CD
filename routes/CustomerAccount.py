from flask import Blueprint
from controllers.CustomerAccount import create, list_all, update_customer_account, delete_customer_account

customer_account_blueprint = Blueprint('customer_account_bp', __name__)
customer_account_blueprint.route('/add', methods=['POST'])(create)
customer_account_blueprint.route('/', methods=['GET'])(list_all)
customer_account_blueprint.route('/update', methods=['PUT'])(update_customer_account)
customer_account_blueprint.route('/delete', methods=['DELETE'])(delete_customer_account)
