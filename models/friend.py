#!/usr/bin/python3
"""
a module that define a user class model
"""
from models.base_model import BaseModel


class Friend(BaseModel):
    """
    a user model class
    """
    def __init__(self, *args, **kwargs):
        """
        initilizes the parent class and itself
        """
        super().__init__()

        self.user_id = ''
        self.friend_id = ''
        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
