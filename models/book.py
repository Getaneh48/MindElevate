#!/usr/bin/python3
"""
a module that define a book model
"""
from models.base_model import BaseModel


class Book(BaseModel):
    """
    a book class model
    """
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
