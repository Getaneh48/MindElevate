#!/usr/bin/python3
"""
a module that define a books reading model
"""
from models.base_model import BaseModel
from datetime import datetime


class BookReading(BaseModel):
    """
    a books reading class model
    """

    def __init__(self, *args, **kwargs):
        """
        initializes the object
        """
        super().__init__()
        self.user_id = ''
        self.book_id = ''
        self.start_date = datetime.utcnow()
        self.pages_per_day = 0
        self.hours_per_day = 0
        self.expected_completion_day = 0
        self.is_favorite = False
        self.friend_visible = False
        self.status = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
