#!/usr/bin/python3
"""
A module that defines a BookMarkBook class
"""
from models.base_model import BaseModel
from datetime import datetime


class BookMarkBook(BaseModel):
    """
    A class representing a bookmarked book.

    Attributes:
        book_id (str): The ID of the bookmarked book.
        bookmarked_date (datetime): The date and time the book was bookmarked.
        bookmarked_by (str): The ID of the user who bookmarked the book.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BookMarkBook instance.

        Args:
            *args: Additional arguments passed to the BaseModel constructor.
            **kwargs: Keyword arguments used to set attributes.
        """
        super().__init__()

        self.book_id = ''
        self.bookmarked_date = datetime.utcnow()
        self.bookmarked_by = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
