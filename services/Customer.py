from sqlalchemy import text, delete
from sqlalchemy.orm import Session
from models.models import db
from models.models import Customer

def create(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            new_customer = Customer(name=customer_data["name"], email=customer_data["email"], phone=customer_data["phone"])
            session.add(new_customer)
            session.commit()

        session.refresh(new_customer)
    return new_customer

def list_all():
    with Session(db.engine) as session:
        with session.begin():
            all_cus = Customer.query.all()
            return all_cus

def list_specific(customer_id):
    with Session(db.engine) as session:
        with session.begin():
            result = Customer.query.filter_by(id=customer_id).first()
            return result

def customer_lifetime_value():
    with Session(db.engine) as session:
        with session.begin():
            response = session.execute(text("SELECT customers.id, customers.name, SUM(total_price) AS total_spending FROM customers INNER JOIN orders WHERE customers.id = orders.customer_id GROUP BY customers.id HAVING SUM(total_price) > 25")).all()
            ret = {}
            for data_idx in range(len(response)):
                r_data = response[data_idx]
                print(r_data)
                ret.update({data_idx: {"customer_id": r_data[0], "customer_name": r_data[1], "total_spending": r_data[2]}})
            return ret

def update_customer(customer_data, customer_id):
    with Session(db.engine) as session:
        with session.begin():
            cur_customer = Customer.query.filter_by(id=customer_id).first()
            cur_customer.name = customer_data["name"]
            cur_customer.email = customer_data["email"]
            cur_customer.phone = customer_data["phone"]
            session.merge(cur_customer)
            session.commit()

    return cur_customer

def delete_customer(customer_id):
    with Session(db.engine) as session:
        with session.begin():
            result = session.execute(delete(Customer).where(Customer.id==customer_id))

    return {"message": "Customer deleted"}
