from flask import request, jsonify
from models.schemas.EmployeeSchema import employee_schema, employees_schema 
from services import Employee
from marshmallow import ValidationError
from utils.util import role_required

@role_required("admin")
def create():
    try:
        employee_data = employee_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    employee_save = Employee.create(employee_data)
    return employee_schema.jsonify(employee_save), 201

def list_all():
    return employees_schema.jsonify(Employee.list_all())
