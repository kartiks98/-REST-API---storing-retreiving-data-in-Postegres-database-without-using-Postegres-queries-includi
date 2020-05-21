# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:52:40 2020

@author: Kartik Saini
"""


from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

# from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from models.user import Blacklist
from resources.user import UserLogin, UserLogout
from db import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgres+psycopg2://postgres:1234@localhost:5432/REST API - stores & items')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = 'access'
app.secret_key = 'key'
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.before_first_request
def create_tables():
    db.create_all()


# jwt = JWT(app, authenticate, identity)  # /auth
jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def check_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in Blacklist


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin,'/login')
api.add_resource(UserLogout,'/logout')

db.init_app(app)
# app.run(port=5000,debug=True)