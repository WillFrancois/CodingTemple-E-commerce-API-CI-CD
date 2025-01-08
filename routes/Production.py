from flask import Blueprint
from controllers.Production import create, list_all, top_selling, production_efficiency

production_blueprint = Blueprint('production_bp', __name__)
production_blueprint.route('/add', methods=['POST'])(create)
production_blueprint.route('/', methods=['GET'])(list_all)
production_blueprint.route('/top_selling', methods=['GET'])(top_selling)
production_blueprint.route('/production_efficiency', methods=['GET'])(production_efficiency)
