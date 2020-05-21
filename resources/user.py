from flask_restful import Resource, reqparse
from models.user import UserModel
from models.user import Blacklist
from flask_jwt_extended import create_access_token,jwt_required,get_raw_jwt

parser = reqparse.RequestParser()
parser.add_argument('username',
                    type=str,
                    required=True,
                    help="This field cannot be blank."
                    )
parser.add_argument('password',
                    type=str,
                    required=True,
                    help="This field cannot be blank."
                    )

class UserRegister(Resource):
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user and user.password == data['password']:
            acces_token = create_access_token(identity = user.id, fresh = True)
        return {'access_token': acces_token}

class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        Blacklist.add(jti)
        return {'message': 'logged out successfully!!!'}








