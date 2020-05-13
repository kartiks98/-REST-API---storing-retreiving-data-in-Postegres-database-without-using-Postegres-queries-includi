# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:24:53 2020

@author: Kartik Saini
"""

from models.user import UserModel
# from werkzeug,security import safe_str_cmp

# users=[
#       {
#         'id':1,
#         'username':'kartik',
#         'password':'abcd'
#         }
#       ]

# username_mapping=[
#     {
#     'kartik':{
#         'id':1,
#         'username':'kartik',
#         'password':'abcd'
#         }
#     }
#     ]

# userid_mapping=[
#     {
#     '1':{
#         'id':1,
#         'username':'kartik',
#         'password':'abcd'
#         }
#     }
#     ]

# users=[
#         User(1001,'kartik','abcd')   #id can be string also
#         ]

# username_mapping={u.username : u for u in users}

# userid_mapping={u.id : u for u in users}

"""JWT will only search for the id attribute in the returned value of 
authenticate function & remembers it for authentication later on when 
identity function is called.

authenticate function parameters can have any name but arguments' names should
be defined specifically as 'username' & 'password' in json format.

JWT does not care of identity function of what it returns but should return 
something so as to vrify JWT that the function is returning something else it 
will give you an error if you did not return anything.""" # - My Observations

def authenticate(username,password):
    user=UserModel.find_by_username(username)
    if user and user.password==password:            
        return user

def identity(payload):
    userid=UserModel.find_by_id(payload['identity'])
    return userid
    # return 'kuchh bhi'


    













