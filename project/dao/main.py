from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User, UserMovies


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(self, page=None, status=None):
        """
        Получить все фильмы из БД
        :param page: страница
        :param status: статус
        :return:
        """
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if status == 'new':
            stmt = stmt.order_by(desc(self.__model__.year))
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


class UserDAO(BaseDAO[User]):
    __model__ = User

    def get_by_email(self, email: str):
        """
        Получить пользователя из БД по email
        :param email: email пользователя
        :return: User
        """
        return self._db_session.query(self.__model__).filter(self.__model__.email == email).first()

    def save(self, user: User):
        """
        Сохранить пользователя
        :param user: User
        """
        self._db_session.add(user)
        self._db_session.commit()
