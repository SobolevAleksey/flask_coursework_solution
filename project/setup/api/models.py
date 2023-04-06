from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

    
auth: Model = api.model('Авторизация', {
    'email': fields.String(required=True, example='alex@yan.com'),
    'password': fields.String(required=True, max_length=100, example='qwerty'),
})

auth_result: Model = api.model('', {
    'access_token': fields.String(required=True),
    'refresh_token': fields.String(required=True),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
    'name': fields.String(),
    'surname': fields.String(),
    'genre': fields.Nested(),
    
})
