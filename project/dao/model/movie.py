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
    trailer = Column(String(100), nullable=False)
    year = Column(String(100), nullable=False)
    rating = Column(String(100), nullable=False)

    genre_id = Column(Integer, ForeignKey(Genre.id), nullable=False)
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey(Director.id), nullable=False)
    director = relationship("Director")
