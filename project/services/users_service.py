from project.dao.user import UserDAO
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        users = self.dao.get_all()
        return users

    def create(self, user_d: dict[str, str]):
        user_d['password'] = generate_password_hash(user_d['password'])
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def update_password(self, email, new_password):
        self.dao.update_password(email, new_password)

    def delete(self, uid):
        self.dao.delete(uid)
