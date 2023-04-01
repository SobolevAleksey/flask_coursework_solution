from sqlite3 import IntegrityError


from project.dao.model.user import User
from project.exceptions import UserAlreadyExists
from project.tools.security import generate_password_hash


# Разбить на разные файлы

class UserDAO:
    def __init__(self, session):
        self.session = session

    # Дублируется?
    def get_one(self, uid):
        return self.session.query(User).get(uid)

    # Дублируется?
    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_d):
        try:
            user = User(**user_d)
            self.session.add(user)
            self.session.commit()
        except IntegrityError:
            raise UserAlreadyExists
        return user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        if user_d.get("email"):
            user.email = user_d.get("email")
        if user_d.get("password"):
            user.email = user_d.get("password")
        if user_d.get("name"):
            user.email = user_d.get("name")
        if user_d.get("surname"):
            user.email = user_d.get("surname")
        try:
            self.session.add(user)
            self.session.commit()
        except IntegrityError:
            raise UserAlreadyExists

    def update_password(self, email, new_password):
        user = self.get_by_email(email)
        user.password = generate_password_hash(new_password)

        self.session.add(user)
        self.session.commit()