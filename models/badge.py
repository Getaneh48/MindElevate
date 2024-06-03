#!/usr/bin/python3
"""
A module that defines a Badge class
"""
from models.base_model import BaseModel


class Badge(BaseModel):
    """
    A class representing a badge.

    Attributes:
        type (str): The type of badge (e.g., "bronze", "silver", "gold").
        icon (str): The URL of the badge icon.
        description (str): A description of the badge.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new Badge instance.

        Args:
            *args: Additional arguments passed to the BaseModel constructor.
            **kwargs: Keyword arguments used to set attributes.
        """
        super().__init__()

        self.type = ''
        self.icon = ''
        self.description = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
