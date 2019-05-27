from flask import Flask, request
from flask_restful import Resource, Api
import mongo_setup as mongo_setup
from controllers.user import add_user

mongo_setup.global_init()

app = Flask(__name__)
api = Api(app)

class UserRoute(Resource):
    def post(self):
        data = request.get_json()
        user = add_user(data.get('username'))
        return {'user': {
            'username': user.username,
            'id': str(user.id)
        }}, 201

api.add_resource(UserRoute, '/users')

if __name__=='__main__':
    app.run(debug=True)
