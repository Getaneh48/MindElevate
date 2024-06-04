#!/usr/bin/python3
"""
a module that define a books reading model
"""
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class BookReading(BaseModel, Base):
    """
    a books reading class model
    """
    __tablename__ = 'book_readings'
    user_id = Column(String(120), ForeignKey('users.id'), nullable=False)
    book_id = Column(String(120), ForeignKey('books.id'), nullable=False)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow())
    pages_per_day = Column(Integer, default=0)
    hours_per_day = Column(Integer, default=0)
    expected_completion_day = Column(Integer, default=0)
    is_favorite = Column(Boolean)
    friend_visible = Column(Boolean)
    status = Column(String(20))
    badge_id = Column(String(120), ForeignKey('badges.id'))
    user = relationship('User', cascade='all, delete', backref='bookreadings')
    book = relationship('Book', cascade='all, delete')
    badge = relationship('Badge', cascade='all, delete')

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
