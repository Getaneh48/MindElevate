#!/usr/bin/python3
"""
A module that define a book share class model
"""
from models.base_model import BaseModel
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, TEXT, ForeignKey
from sqlalchemy.orm import relationship


class RecommendBook(BaseModel, Base):
    """
    A class representing a book that will be shared
    """
    __tablename__ = 'recommended_books'
    user_id = Column(String(120), ForeignKey('users.id'), nullable=False)
    recommender_id = Column(String(120), nullable=False)
    book_id = Column(String(120), ForeignKey('books.id'), nullable=False)
    description = Column(TEXT)
    user  = relationship('User', cascade='all', backref='books_recommended')

    def __init__(self, *args, **kwargs):
        """
        initializes a share book object

        Args:
            args (list): list of arguments
            kwargs (dict): dictionary of keyword arguments
        """
        super().__init__()
        self.book_id = ''
        self.recommender_id = ''
        self.user_id= ''
        self.description = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
