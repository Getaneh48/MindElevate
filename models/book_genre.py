#!/usr/bin/python3
"""
The module defines books genre.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column


class BookGenre(BaseModel, Base):
    """
    A class that represents a book genre
    """
    __tablename__ = 'book_genres'
    name = Column(String(120), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        initializes the object
        """
        super().__init__()
        self.name = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
