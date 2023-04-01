import calendar
import datetime

import jwt
from flask import abort, current_app

from project.services.users_service import UsersService
from project.tools.security import compare_passwords


class AuthService:

    def __init__(self, user_service: UsersService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=True):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise abort(404)
        if not is_refresh:
            if not compare_passwords(user.password, password):
                abort(404)

        data = {
            'email': user.email
        }

        # Токен на 30 мин
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
                                  algorithm=current_app.config['JWT_ALGORITHM'])
        # Токен на 130 дней
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
                                   algorithm=current_app.config['JWT_ALGORITHM'])
        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token,
                          key=current_app.config['SECRET_KEY'],
                          algorithm=current_app.config['JWT_ALGORITHM'])
        email = data.get('email')

        user = self.user_service.get_by_email(email=email)
        if user is None:
            raise Exception()
        return self.generate_tokens(email, user.password, is_refresh=True)


