import jwt
from datetime import datetime, timedelta
from flask import current_app


def generate_token(user_id):
    
    secret_key = current_app.config["SECRET_KEY"]
    expiration_time = datetime.utcnow() + timedelta(days=90)
    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def decode_token(token):
    
    try:
        secret_key = current_app.config["SECRET_KEY"]
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    
def Checkauth(token):
    try:
        decode = decode_token(token)
        if decode:
            return decode["user_id"]
        return None
    except Exception as e:
        return e