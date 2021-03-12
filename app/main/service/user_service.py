import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.main import db
from app.main.model.user import Subscription, AdminUser


def subscribe_user(data):
    """
    Add new user to subscription database
    """
    user = Subscription.query.filter_by(email=data['email']).first()
    if not user:
        user = Subscription(data['email'], public_id=uuid.uuid4())
        db.session.add(user)
        db.session.commit()
        # app.logger.info('%s : successfully subscribed', user.email)
        status = 201
        change = True
        new = True
        message = 'user added to database'
    else:
        # app.logger.info('%s : User already exist', user.email)
        status = 200
        change = False
        new = False
        message = 'User already exist in database'

    user = {
        'id': user.id,
        'mail': user.email,
        'timeStamp': user.timestamp,
        'subscribed': user.subscription
    }
    return {
        'status': status,
        'change': change,
        'new': new,
        'message': message,
        'user': user
    }


def change_subscription(data):
    """
    Change subscription database
    """
    update_this = db.session.query(Subscription).filter_by(email=data['email']).first()
    if update_this:
        update_this.subscription = not update_this.subscription
        update_this.timestamp = datetime.now()
        db.session.commit()
        # app.logger.warning('%s : Subscription Changed', data['email'])
        status = 200
        change = True
        message = 'Subscription changed'
        email = update_this.email
        new_state = update_this.subscription

    else:
        # app.logger.warning('%s : User not exist', data['email'])
        status = 404
        change = True
        message = 'User not exist'
        email = data['email']
        new_state = None

    response_object = {
        'status': status,
        'change': change,
        'message': message,
        'email': email,
        'new_sub_state': new_state
    }
    return response_object, status


def save_admin_user(data):
    """
    save new admin user to database
    """
    admins = AdminUser.query.filter_by(email=data['email']).first()
    if not admins:
        user = AdminUser(first_name=data['fname'],
                         last_name=data['lname'],
                         public_id=uuid.uuid4(),
                         email=data['email'],
                         password=generate_password_hash(data['password']))
        db.session.add(user)
        db.session.commit()
        response_object = {
            'success': True,
            'message': 'Successfully registered.'
        }
        return response_object, 201

    else:
        response_object = {
            'success': False,
            'message': 'User already exists with this email. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    """
    return all admin users
    """
    return {'users': AdminUser.query.all()}, 200


def get_user(id):
    """
    return admin user using id
    """
    return AdminUser.query.filter_by(id=id).first(), 200
