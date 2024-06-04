#!/usr/bin/python3
"""
A module that defines a BookReview class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class BookReview(BaseModel, Base):
    """
    A class representing a book review

    Attributes:
        book_id (str): The id of the book being reviewed.
        reviewer_id (str): The id of the user who wrote the review
        description (str): The text of the book review
    """
    __tablename__ = 'book_reviews'
    book_id = Column(String(120), ForeignKey('books.id'), nullable=False)
    reviewer_id = Column(String(120), ForeignKey('users.id'), nullable=False)
    description = Column(String(254), nullable=False)
    book = relationship('Book')
    reviewer = relationship('User', cascade='all, delete', backref='books_reviewed')

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BookReview instance.

        Args:
            *args: Additional arguments passed to the BaseModel constructor.
            **kwargs: Keyword arguments used to set attributes.
        """
        super().__init__()

        self.book_id = ''
        self.reviewer_id = ''
        self.description = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
