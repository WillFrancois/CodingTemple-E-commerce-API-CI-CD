from services import User
from flask import jsonify, request

def login():
    data = request.json
    print("Data: ", data)
    user = User.login_customer(str(data["username"]), str(data["password"]))
    print("User:", user)
    if user:
        return jsonify(user), 200
    else:
        resp = {
            "status":"Error",
            "message":"User does not exist!"
        }
        return jsonify(resp), 404
