from flask_restx import Namespace, Resource
from project.setup.api.models import user
from project.container import users_service

# Реализуем следующие эндпоинты:

#- **GET** /user/ — получить информацию о пользователе (его профиль).
#- **PATCH** /user/ — изменить информацию пользователя (имя, фамилия, любимый жанр).
#- **PUT** /user/password — обновить пароль пользователя, для этого нужно отправить два пароля *password_1* и *password_2.*

#Для того чтобы все  ссылки корректно работали, их нужно обернуть в декоратор, в котором мы будет проверять переданный токен.

user_ns = Namespace('user')

@user_ns.route('/')
class UserView(Resource):
    def get(self, user_id):
        return user_service.get_one(user_id)
        
    def patch(self,user_d):
        return user_service.update(user_d)
        



#@user_ns.route('/password/')
#class UserView(Resource):
    def put(self, password_1 and password_2):
        data = request.json
        pass

