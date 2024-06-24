#!/usr/bin/python3
"""
a module that define a books reading model
"""
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import models


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
    is_liked = Column(Boolean)
    friend_visible = Column(Boolean)
    status = Column(String(20), default="on progress")
    badge_id = Column(String(120), ForeignKey('badges.id'))
    user = relationship('User', backref='booksreading')
    book = relationship('Book')
    badge = relationship('Badge')

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
        self.is_liked = False
        self.friend_visible = False
        self.status = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def readingOnProgress(self):
        onprogress = models.storage.readingOnProgress(self)
        print(onprogress)
