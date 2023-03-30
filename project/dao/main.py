from project.dao.base import BaseDAO
from project.models import Genre


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre

 # Разбить на разные файлы    
class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director

class UsersDAO(BaseDAO[User]):
    __model__ = User

class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie




