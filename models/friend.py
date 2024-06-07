#!/usr/bin/python3
"""
a module that define a user class model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class Friend(BaseModel, Base):
    """
    a user model class
    """
    __tablename__ = 'friends'
    # friend_id = Column(String(120), ForeignKey('users.id'), nullable=False)
    user_id = Column(String(120), ForeignKey('users.id'), nullable=False)
    friend_id = Column(String(120), nullable=False)
    user = relationship('User', cascade='all, delete', backref='friends')

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
