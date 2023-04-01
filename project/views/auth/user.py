from flask_restx import Namespace, Resource
from project.dao import user
from project.services import users_service

user_ns = Namespace('user')

@user_ns.route('/')
class UserView(Resource):
    @user_ns.expect(user)
    #@user_ns.response(201, description='OK')
    def get(self):
        pass
    def patch(self):
        pass



@user_ns.route('/password/')
class UserView(Resource):
    def put(self):
        pass

