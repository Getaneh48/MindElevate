#!/usr/bin/python3
"""
a module that define a books reading log model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class ReadingLog(BaseModel, Base):
    """
    a books reading log class model
    """
    __tablename__ = 'reading_logs'
    br_id = Column(String(120), ForeignKey('book_readings.id'), nullable=False)
    pages_read = Column(Integer, nullable=False)
    hours_read = Column(Integer, nullable=False)
    status = Column(String(50), nullable=True)
    badge_id = Column(String(120), ForeignKey('badges.id'), nullable=True)
    book_reading = relationship('BookReading', cascade='all, delete', backref='reading_logs')
    badge = relationship('Badge', backref='badge')

    def __init__(self, *args, **kwargs):
        """
        initializes the object
        """
        super().__init__()
        self.br_id = ''
        self.pages_read = 0
        self.hours_read = 0
        self.badge_id = ''
        self.status = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
