#!/usr/bin/python3
"""
This module defines a User class model that inherits from the BaseModel class.
The User class represents a user entity with various attributes such as username,
password, personal information, age, gender, profile picture, and book
genre preferences.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class representing a user entity.

    Args:
        *args: Variable length argument list (not used in this implementation).
        **kwargs: Keyword arguments used to initialize attributes.

    Attributes:
        username (str): The username of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        age (int): The age of the user.
        sex (str): The gender of the user.
        picture (str): The profile picture URL or path of the user.
        book_genre_prefs (list): A list of preferred book genres for the user.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the User object with default attribute values and updates
        them with provided keyword arguments.

        Args:
            *args: Variable length argument list (not used in this implementation).
            **kwargs: Keyword arguments used to initialize attributes.

        Returns:
            None
        """
        super().__init__()

        self.username = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        self.age = ''
        self.sex = ''
        self.picture = ''
        self.book_genere_prefs = []

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
