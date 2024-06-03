#!/usr/bin/python3
"""
A module that define a book share class model
"""
from models.base_model import BaseModel


class ShareBook(BaseModel):
    """
    A class representing a book that will be shared
    """

    def __init__(self, *args, **kwargs):
        """
        initializes a share book object

        Args:
            args (list): list of arguments
            kwargs (dict): dictionary of keyword arguments
        """
        super().__init__()
        self.book_id = ''
        self.use_id = ''
        self.shared_user_id = ''
        self.description = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
