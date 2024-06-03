#!/usr/bin/python3
"""
A module that defines a BookReview class
"""
from models.base_model import BaseModel


class BookReview(BaseModel):
    """
    A class representing a book review

    Attributes:
        book_id (str): The id of the book being reviewed.
        reviewer_id (str): The id of the user who wrote the review
        description (str): The text of the book review
    """
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
