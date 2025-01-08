from services import User
from flask import jsonify, request

def login():
    data = request.json
    user = User.login_customer(data["username"], data["password"])
    if user:
        return jsonify(user), 200
    else:
        resp = {
            "status":"Error",
            "message":"User does not exist!"
        }
        return jsonify(resp), 404
