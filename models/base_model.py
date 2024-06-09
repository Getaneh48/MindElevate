#!/usr/bin/python3
from datetime import datetime
import uuid
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """
    Base class for all models in the application.

    Attributes:
        id (str): A unique identifier for the object.
        created_at (datetime): The datetime the object was created.
        updated_at (datetime): The datetime the object was last updated.
    """
    id = Column(String(120), nullable=False, default=str(uuid.uuid4()), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self):
        """
        Initializes a new BaseModel instance.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return (f"[{self.__class__.__name__}] {self.id} {self.to_dict()}")

    def to_dict(self):
        """
        Returns a dictionary representation of the object's attributes.
        """
        dictionary = {}
        dictionary.update(self.__dict__.copy())

        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']

        for key in dictionary.keys():
            if isinstance(dictionary[key], datetime):
                dictionary[key] = dictionary[key].strftime("%Y-%m-%dT%H:%M:%S.%f")

        return dictionary

    def __repr__(self):
        """
        Returns a string representation of the object suitable
        for code execution.
        """
        arg = {**self.to_dict()}
        return (f"{self.__class__.__name__}({arg})")

    def add(self):
        self.updated_at = datetime.utcnow()
        models.storage.add(self)

    def save(self):
        """
        Saves the object to the storage engine.
        """
        models.storage.save()

    def all(self):
        """
        Returns a list of all objects of the current class or a specific class.

        Args:
            cls (class, optional): The class to retrieve objects for.
                                    Defaults to None, which returns all objects
                                    of the current class.

        Returns:
            list: A list of objects.
        """
        return models.storage.all(self.__class__.__name__)

    def get(self):
        """
        Retrieves an object from the storage engine.

        Args:
            cls (class or str, optional): The class of the object to retrieve,
                                         or the class name as a string.
                                         Defaults to None, which retrieves the
                                         current object.
            oid (str, optional): The id of the object to retrieve. Defaults
                                 to None, which retrieves the current object.

        Returns:
            object: The retrieved object, or None if not found.
        """
        return models.storage.get(self.__class__.__name__, self.id)

    def delete(self):
        """
        Deletes the object from the storage engine.
        """
        models.storage.delete(self)
