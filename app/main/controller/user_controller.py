from flask import request, make_response, jsonify
from flask_restplus import Resource
from werkzeug.security import check_password_hash
from app.main.model.user import AdminUser
from app.main.service.user_service import subscribe_user, change_subscription, save_admin_user, get_all_users, get_user
from app.main.util.dto import UserDto
import datetime
import jwt
from app.main.config import Config
from app.main.model.token import token_required

api = UserDto.api
_user = UserDto.user_sub
_update = UserDto.update_sub
_save_admin = UserDto.save_admin
_admin_users = UserDto.admin_users
_admin_model = UserDto.admin_model

_req_subscriber = UserDto.req_subscriber
_req_get_admin = UserDto.req_get_admin
_req_save_admin = UserDto.req_save_admin
_req_get_all = UserDto.req_get_all


@api.route('api/subscription')
class InsertUser(Resource):
    @api.expect(_req_subscriber)
    @api.marshal_with(_user)
    def post(self):
        """Creates a new User """
        data = request.json
        return subscribe_user(data=data)

    @api.expect(_req_subscriber)
    @api.doc("Update User")
    @api.marshal_with(_update)
    def put(self):
        """Change Subscription of user """
        data = request.json
        return change_subscription(data=data)


@api.route('aapi/admin')
class User(Resource):
    @api.expect(_req_save_admin)
    @api.doc("Insert admin User")
    @api.marshal_with(_save_admin)
    def post(self):
        """
        Insert new admin user to database
        """
        data = request.json
        print(data)
        return save_admin_user(data=data)

    @api.expect(_req_get_all)
    @api.doc('list_of_registered_admin_users')
    @api.marshal_list_with(_admin_users, envelope='data')
    def get(self):
        """
        Fetch all admin users from database
        """
        return get_all_users()


@api.route('aapi/admin/get')
class User(Resource):
    @api.expect(_req_get_admin)
    @api.doc('get a user')
    @token_required
    def get(self, current_user):
        """get a user using given identifier"""
        print("SAAAAAa")
        print(self, current_user)
        data = request.json
        user = get_user(data['id'])
        if not user:
            api.abort(404)
        else:
            return user


@api.route('aapi/v1.0/signin')
class AdminSignIn(Resource):
    def post(self):
        data = request.json
        if not data or not data['username'] or not data['password']:
            return make_response(
                'could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
        user = AdminUser.query.filter_by(email=data['username']).first()
        if not user:
            return make_response(
                'could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
        if check_password_hash(user.password, data['password']):
            token = jwt.encode(
                {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                Config.SECRET_KEY)
            return jsonify(
                {'token': token, "first_name": user.first_name, "second_name": user.last_name,
                 "user_email": user.email})
        return make_response(
            'could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
