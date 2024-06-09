#!/usr/bin/python3
"""
A module that defines a Badge class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, TEXT


class Badge(BaseModel, Base):
    """
    A class representing a badge.

    Attributes:
        type (str): The type of badge (e.g., "bronze", "silver", "gold").
        icon (str): The URL of the badge icon.
        description (str): A description of the badge.
    """
    __tablename__ = 'badges'
    btype = Column(String(100), nullable=False, unique=True)
    icon = Column(String(254), nullable=True)
    description = Column(TEXT, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Badge instance.

        Args:
            *args: Additional arguments passed to the BaseModel constructor.
            **kwargs: Keyword arguments used to set attributes.
        """
        super().__init__()

        self.btype = ''
        self.icon = ''
        self.description = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
