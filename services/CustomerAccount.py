from sqlalchemy import text, delete
from sqlalchemy.orm import Session
from models.models import db
from models.models import CustomerAccount
from hashlib import sha256

def create(customer_account_data):
    with Session(db.engine) as session:
        with session.begin():
            # Password is a potential example of a hashing algorithm; SHA256 is no longer recommended even if salted
            new_customer_account = CustomerAccount(username=customer_account_data["username"], password=sha256(customer_account_data["password"].encode("utf-8")).hexdigest(), customer_id=customer_account_data["customer_id"])
            session.add(new_customer_account)
            session.commit()

        session.refresh(new_customer_account)
    return new_customer_account

def list_all():
    with Session(db.engine) as session:
        with session.begin():
            all_cus = CustomerAccount.query.all()
            return all_cus

def update_customer_account(customer_account_data, customer_account_id):
    with Session(db.engine) as session:
        with session.begin():
            cur_account = CustomerAccount.query.filter_by(id=customer_account_id).first()
            cur_account.username = customer_account_data["username"]
            cur_account.password = sha256(customer_account_data["password"].encode("utf-8")).hexdigest()
            cur_account.customer_id = customer_account_data["customer_id"]
            session.merge(cur_account)
            session.commit()

    return cur_account

def delete_customer_account(customer_account_id):
    with Session(db.engine) as session:
        with session.begin():
            result = session.execute(delete(CustomerAccount).where(CustomerAccount.id==customer_account_id))

    return {"message": "Account deleted"}
