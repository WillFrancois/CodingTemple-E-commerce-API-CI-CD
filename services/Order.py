from sqlalchemy import select, text
from sqlalchemy.orm import Session
from models.models import db
from models.models import Order

def create(order_data):
    with Session(db.engine) as session:
        with session.begin():
            new_order = Order(customer_id=order_data["customer_id"], product_id=order_data["product_id"], quantity=order_data["quantity"], total_price=order_data["total_price"])
            session.add(new_order)
            session.commit()

        session.refresh(new_order)
    return new_order

def list_all(page, per_page):
    with Session(db.engine) as session:
        with session.begin():
            #Implementing Pagination in the Factory Management System
            #Task 1
            all_order = db.paginate(select(Order), page=page, per_page=per_page)
            return all_order

