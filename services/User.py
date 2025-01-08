from sqlalchemy import select
from sqlalchemy.orm import Session
from utils.util import encode_token
from models.models import db
from models.models import User

def login_customer(username, password):
    user = (db.session.execute(db.select(User).where(User.username == username, User.password == password)).scalar_one_or_none())
    role_name = user.role
    if user:
        auth_token = encode_token(user.id, role_name)
        resp = {
            "status":"success",
            "message":"Login successful",
            "auth_token":auth_token
        }
        return resp
    else:
        return None
