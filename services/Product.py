from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from models.models import db
from models.models import Product

def create(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data["name"], price=product_data["price"])
            session.add(new_product)
            session.commit()

        session.refresh(new_product)
    return new_product

def list_all(page, per_page):
    with Session(db.engine) as session:
        with session.begin():
            all_prod = db.paginate(select(Product), page=page, per_page=per_page)
            return all_prod

def list_specific(product_id):
    with Session(db.engine) as session:
        with session.begin():
            result = Product.query.filter_by(id=product_id).first()
            return result

def update_product(product_data, product_id):
    with Session(db.engine) as session:
        with session.begin():
            cur_product = Product.query.filter_by(id=product_id).first()
            cur_product.name = product_data["name"]
            cur_product.price = product_data["price"]
            session.merge(cur_product)
            session.commit()

    return cur_product

def delete_product(product_id):
    with Session(db.engine) as session:
        with session.begin():
            session.execute(delete(Product).where(Product.id==product_id))
            session.commit()

    return {"message": "Product deleted"}
