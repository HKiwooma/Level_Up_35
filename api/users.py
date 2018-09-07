from flask import jsonify, Blueprint

from flask.ext.restful import Resource, Api

class UserList(Resource):
    def add_user(self,id):
        return jsonify([['users': [{'name': 'haruna'}]])

class User(Resource):
    def get_user(self, id):
        return jsonify({'name': 'haruna'})
    
    # def put(self, id):
    #     return jsonify({'name': 'kiwooma'})
    
    def delete_user(self, id):
        return jsonify({'name': 'haruna'})

users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(
    UserList,
    '/api/add-user',
    endpoint='add-user'
)