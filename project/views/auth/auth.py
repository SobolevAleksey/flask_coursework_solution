from flask_restx import Namespace, Resource
from flask import request, abort
from project.services import users_service, auth_service
from project.views import auth

auth_ns = Namespace('auth')


@auth_ns.route('/register/')  # Регитсрация создание пользователя в БД
class AuthView(Resource):
    @auth_ns.expect(auth)
    @auth_ns.response(201, description='OK')
    def post(self):
        users_service.create(request.json)
        return "OK", 201


@auth_ns.route('/login/')
class AuthsView(Resource):

    @auth_ns.expect(auth)
    # @auth_ns.marshal_with(auth_result, code=200)
    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            abort(400)

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 200

    def put(self):
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)

        return tokens, 200
