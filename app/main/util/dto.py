from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user_model = api.model("subscription", {
        'id': fields.Integer(required=True, description='user id in database'),
        'mail': fields.String(required=True, description='user mail id'),
        'timeStamp': fields.DateTime(required=True, description='time stamp'),
        'subscribed': fields.Boolean(required=True, description='subscription status'),
    })
    user_sub = api.model('subscribe_user', {
        'status': fields.Integer(required=True, description='status code'),
        'change': fields.Boolean(required=True, description='change in database'),
        'new': fields.Boolean(required=True, description='is user in new'),
        'message': fields.String(required=True, description='message'),
        'user': fields.List(fields.Nested(user_model))
    })
    update_sub = api.model('update_subscription', {
        'status': fields.Integer(required=True, description='status code'),
        'change': fields.Boolean(required=True, description='change in database'),
        'message': fields.String(required=True, description='message'),
        'email': fields.String(required=True, description='user mail id'),
        'new_sub_state': fields.Boolean(required=True, description='new sub state')
    })

    save_admin = api.model('admin_save', {
        'success': fields.Integer(required=True, description='if success: True else: False '),
        'message': fields.String(required=True, description='message')
    })

    admin_model = api.model('get_single_admin', {
        'first_name': fields.String(required=True, description='message'),
        'last_name': fields.String(required=True, description='message'),
        'email': fields.String(required=True, description='message'),
    })
    admin_users = api.model('all_admins', {
        'users': fields.List(fields.Nested(admin_model))
    })

    req_subscriber = api.model("new_user", {
        'email': fields.String(required=True, description='user mail id')
    })

    req_save_admin = api.model("save new admin user", {
        'fname': fields.String(required=True, description='user mail id'),
        'lname': fields.String(required=True, description='user mail id'),
        'email': fields.String(required=True, description='user mail id'),
        'password': fields.String(required=True, description='user mail id')
    })
    req_get_all = api.model("Get all Admins", {})

    req_get_admin = api.model("get_admin", {
        'id': fields.Integer(required=True, description='user id in database', default=1),
        'message': fields.String(required=True, description='message')
    })

    req_sign_in = api.model("Sign in", {
        "username": fields.String(required=True, description='email id'),
        "password": fields.String(required=True, description='user password')
    })
