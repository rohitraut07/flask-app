import jwt
from flask import request, jsonify
from app.main.config import Config
from functools import wraps
from app.main.model.user import AdminUser


def token_required(f):


    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
            print(token)
        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            current_user = AdminUser.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
