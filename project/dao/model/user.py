from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from project.dao.model.genre import Genre
from project.setup.db import models


class User(models.Base):
    """
    Создаем класс - пользователь.
    """
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))

    #favorite_genre = Column(Integer, ForeignKey(Genre.id))
    #genre = relationship("Genre")
