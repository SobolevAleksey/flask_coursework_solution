from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from project.dao.model.director import Director
from project.dao.model.genre import Genre
from project.setup.db import models


class Movie(models.Base):
    """
    Создаем класс - фильмы.
    """
    __tablename__ = 'movies'

    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    trailer = Column(String(100), unique=True, nullable=False)
    year = Column(String(100))
    rating = Column(String(100))

    genre_id = Column(Integer, ForeignKey(Genre.id))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey(Director.id))
    director = relationship("Director")
