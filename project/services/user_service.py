from flask import abort
from project.dao.main import UserDAO, GenresDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_password_hash, compose_passwords


class UsersService:
    def __init__(self, user_dao: UserDAO, genre_dao: GenresDAO) -> None:
        self.user_dao = user_dao
        self.genres_dao = genre_dao

    def get_item(self, pk: int) -> User:
        if user := self.user_dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_by_email(self, email: str) -> User:
        if user := self.user_dao.get_by_email(email):
            return user
        raise ItemNotFound(f'User with email={email} not exists.')

    def create(self, data):
        data['password'] = generate_password_hash(data.get('password'))

        if self.is_user(data.get('email')):
            abort(400)
        new_user = User(**data)
        self.user_dao.save(new_user)

    def is_user(self, email):
        return bool(self.user_dao.get_by_email(email))

    def update_partial(self, data):
        user = self.get_by_email(data['email'])

        if 'name' in data:
            user.name = data.get('name')
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'favorite_genre_id' in data:
            genre = self.genres_dao.get_by_id(data['favorite_genre_id'])
            user.genre = genre
        self.user_dao.save(user)

    def change_password(self, user_data):
        user = self.get_by_email(user_data['email'])
        password = user_data['password_1']

        if compose_passwords(user.password, password):
            new_password = generate_password_hash(user_data['password_2'])
            user.password = new_password
            self.user_dao.save(user)
        else:
            return abort(403)
