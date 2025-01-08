from flask import Blueprint
from controllers.Employee import create, list_all

employee_blueprint = Blueprint('employee_bp', __name__)
employee_blueprint.route('/add', methods=['POST'])(create)
employee_blueprint.route('/', methods=['GET'])(list_all)
