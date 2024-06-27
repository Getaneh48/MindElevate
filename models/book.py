#!/usr/bin/python3
"""
a module that define a book model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Book(BaseModel, Base):
    """
    a book class model
    """
    __tablename__ = 'books'
    title = Column(String(120), nullable=False)
    author = Column(String(length=500), nullable=False)
    genre_id = Column(String(120), ForeignKey("book_genres.id"),
                      nullable=False)
    pub_year = Column(Integer, nullable=False)
    pages = Column(Integer, nullable=False)
    cover_image = Column(String(254))
    subtitle = Column(String(length=500))
    description = Column(String(length=1000))
    genre = relationship('BookGenre')

    def __init__(self, *args, **kwargs):
        """
        initializes the object
        """
        super().__init__()
        self.title = ''
        self.author = ''
        self.pub_year = ''
        self.pages = 0
        self.cover_image = ''
        self.subtitle = ''
        self.description = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
