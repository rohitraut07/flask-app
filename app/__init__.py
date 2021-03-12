# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from app.main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='ProjectOperations',
          version='1.0',
          description=''
          )

api.add_namespace(user_ns, path='/')
