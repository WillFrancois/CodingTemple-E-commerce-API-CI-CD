# Task 2
from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv
from flask import request, jsonify
from functools import wraps

# NOTE: My .env file is named differently as my venv folder is labeled as .env
load_dotenv('.envfile')
SECRET_KEY = os.getenv('SECRET_KEY')

def encode_token(user_id, role_name):
    payload = {
        'exp': datetime.now() + timedelta(days=100),
        'iat': datetime.now(),
        'sub': user_id,
        'role': role_name
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        print(payload)
    except jwt.ExpiredSignatureError as e:
        print(e)
    except jwt.InvalidTokenError as e:
        print(e)

    return token

def role_required(needed_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = None
            if "Authorization" in request.headers:
                token = str(request.headers["Authorization"].split(" ")[1])
            if not token:
                return jsonify({'message': 'Token is missing'}), 401

            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401
            except jwt.InvalidTokenError as e:
                print(e)
                return jsonify({'message': 'Invalid token'}), 401

            role = payload['role']

            if role != needed_role:
                return jsonify({'message': 'User role does not match'})

            return f(*args, **kwargs)

        return decorated_function

    return decorator
