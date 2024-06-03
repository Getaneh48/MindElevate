#!/usr/bin/python3
"""
a module that define a books reading log model
"""
from models.base_model import BaseModel


class ReadingLog(BaseModel):
    """
    a books reading log class model
    """

    def __init__(self, *args, **kwargs):
        """
        initializes the object
        """
        super().__init__()
        self.br_id = ''
        self.pages_read = 0
        self.hours_read = 0

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
