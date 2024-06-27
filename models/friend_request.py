#!/usr/bin/python3
"""
a module that define a friend request class model
"""
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class FriendRequest(BaseModel, Base):
    """
    A class representing a friend request
    """
    __tablename__ = 'friend_requests'
    request_from = Column(String(120), nullable=False)
    request_to = Column(String(120), ForeignKey('users.id'), nullable=False)
    request_date = Column(DateTime, default=datetime.utcnow())
    status = Column(String(20), default='pending')
    message = Column(String(2554))
    requested_user = relationship('User', backref='friend_requests')

    def __init__(self, *args, **kwargs):
        """
        A constructor method to initialize attributes of the object
        """
        super().__init__()

        self.request_from = ''
        self.request_to = ''
        self.request_date = datetime.utcnow()
        self.status = ''  # accepted , rejected, pending
        self.message = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
