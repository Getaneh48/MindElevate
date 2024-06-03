#!/usr/bin/python3
"""
a module that define a friend request class model
"""
from models.base_model import BaseModel
from datetime import datetime

class FriendRequest(BaseModel):
    """
    
    """
    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__()

        self.request_from = ''
        self.request_to = ''
        self.request_date = datetime.utcnow()

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
