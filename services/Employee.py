from sqlalchemy.orm import Session
from models.models import db
from models.models import Employee

def create(employee_data):
    with Session(db.engine) as session:
        with session.begin():
            new_employee = Employee(name=employee_data["name"], position=employee_data["position"])
            session.add(new_employee)
            session.commit()

        session.refresh(new_employee)
    return new_employee

def list_all():
    with Session(db.engine) as session:
        with session.begin():
            all_emp = Employee.query.all()
            return all_emp
