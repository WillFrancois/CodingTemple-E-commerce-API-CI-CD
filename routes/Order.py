from flask import Blueprint
from controllers.Order import create, list_all

order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/add', methods=['POST'])(create)
order_blueprint.route('/', methods=['GET'])(list_all)
