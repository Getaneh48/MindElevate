#!/usr/bin/python3
"""
A module that defines a BookMarkBook class
"""
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class FavouriteBook(BaseModel, Base):
    """
    A class representing a favourite book of a user.

    Attributes:
        book_id (str): The ID of the bookmarked book.
        user_id (str): The ID of the user who mark the book as a favourite.
    """
    __tablename__ = 'favourite_books'
    book_id = Column(String(120), ForeignKey('books.id'), nullable=False, unique=True)
    user_id = Column(String(120), ForeignKey('users.id'), nullable=False)
    book = relationship('Book')
    user = relationship('User', backref='favourite_books')

    def __init__(self, *args, **kwargs):
        """
        Initializes a new FavouriteBook instance.

        Args:
            *args: Additional arguments passed to the BaseModel constructor.
            **kwargs: Keyword arguments used to set attributes.
        """
        super().__init__()

        self.book_id = ''
        self.user_id = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
