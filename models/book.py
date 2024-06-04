#!/usr/bin/python3
"""
a module that define a book model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer


class Book(BaseModel, Base):
    """
    a book class model
    """
    __tablename__ = 'books'
    title = Column(String(120), nullable=False)
    author = Column(String(120), nullable=False)
    genere = Column(String(30), nullable=False)
    pub_year = Column(Integer, nullable=False)
    pages = Column(Integer, nullable=False)
    cover_image = Column(String(254))

    def __init__(self, *args, **kwargs):
        """
        initializes the object
        """
        super().__init__()
        self.title = ''
        self.author = ''
        self.genere = ''
        self.pub_year = ''
        self.pages = 0
        self.cover_image = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
