from sqlalchemy import text
from sqlalchemy.orm import Session
from models.models import db
from models.models import Production, Product

def create(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production = Production(product_id=production_data["product_id"], quantity_produced=production_data["quantity_produced"], date_produced=production_data["date_produced"])
            session.add(new_production)
            session.commit()

        session.refresh(new_production)
    return new_production

def list_all():
    with Session(db.engine) as session:
        with session.begin():
            all_production = Production.query.all()
            print(all_production)
            return all_production

def top_selling():
    with Session(db.engine) as session:
        with session.begin():
            response = session.execute(text("SELECT products.name, SUM(production.quantity_produced) FROM production JOIN products WHERE products.id = production.product_id GROUP BY production.product_id ORDER BY SUM(production.quantity_produced) DESC")).all()
            ret = {}
            for data_idx in range(len(response)):
                r_data = response[data_idx]
                print(r_data)
                ret.update({data_idx: {"product_name": r_data[0], "quantity_produced": r_data[1]}})
            return ret

def production_efficiency():
    with Session(db.engine) as session:
        with session.begin():

            response = session.execute(text("SELECT products.name, production.product_id, SUM(quantity_produced) FROM products INNER JOIN production WHERE products.id = production.product_id AND date_produced = '2014-01-01' GROUP BY production.product_id")).all()
            ret = {}
            for data_idx in range(len(response)):
                r_data = response[data_idx]
                print(r_data)
                ret.update({data_idx: {"product_name": r_data[0], "product_id": r_data[1], "quantity_produced": r_data[2]}})
            return ret
