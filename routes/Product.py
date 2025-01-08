from flask import Blueprint
from controllers.Product import create, list_all, update_product, delete_product, list_specific

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/add', methods=['POST'])(create)
product_blueprint.route('/', methods=['GET'])(list_all)
product_blueprint.route('/update', methods=['PUT'])(update_product)
product_blueprint.route('/delete', methods=['DELETE'])(delete_product)
product_blueprint.route('/find', methods=['GET'])(list_specific)
