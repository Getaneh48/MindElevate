#!/usr/bin/python3
import json
from models.user import User
from models.book import Book
from models.badge import Badge
from models.book_review import BookReview
from models.bookmark_book import BookMarkBook
from models.friend import Friend
from models.friend_request import FriendRequest
from models.book_reading import BookReading
from models.reading_log import ReadingLog
from models.share_book import ShareBook
from models.base_model import BaseModel
from models.book_genre import BookGenre
import os
from datetime import datetime


class FileStorage:
    """
    FileStorage class that handles the storage and retrieval of objects
    in a JSON file. It provides methods for loading, saving, adding,
    retrieving, and deleting objects.

    Attributes:
        __objects (dict): A dictionary to store all objects in the system.
                          The key is a string in the format
                          "class_name.object_id" , and the value is the
                          corresponding object instance.
        __file_path (str): The path to the JSON file where objects are stored.
        __classes (dict): A dictionary mapping class names to their
                          corresponding class objects.
        __time_f (str): The format string used for serializing and
                        deserializing datetime objects.
    """

    __objects = {}
    __file_path = 'test_file.json'
    __classes = {'User': User,
                 'Book': Book,
                 'BookGenre': BookGenre,
                 'BookReading': BookReading,
                 'ReadingLog': ReadingLog,
                 'ShareBook': ShareBook,
                 'Badge': Badge,
                 'Friend': Friend,
                 'FriendRequest': FriendRequest,
                 'BookReview': BookReview,
                 'BookMarkBook': BookMarkBook}

    __time_f = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self):
        """
        Initializes the FileStorage object by loading objects from
        the JSON file.
        """
        self.load()

    def load(self):
        """
        Loads objects from the JSON file into the __objects dictionary.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                if objs:
                    for key, val in objs.items():
                        cls_name = key.split('.')[0]
                        if cls_name in self.__classes.keys():
                            obj = self.__classes[cls_name](**val)
                            obj.created_at = datetime.strptime(obj.created_at,
                                                               self.__time_f)
                            obj.updated_at = datetime.strptime(obj.updated_at,
                                                               self.__time_f)
                            self.__objects[key] = obj
        else:
            pass

    def all(self, cls=None):
        """
        Returns a list of all objects in the system, or all objects
        of a specific class.

        Args:
            cls (class, optional): The class of objects to retrieve.
                                   Defaults to None,
                                   which returns all objects.

        Returns:
            list: A list of objects.
        """
        if cls:
            cls_objects = {}
            for key in self.__objects:
                cname = key.split('.')[0]
                if cname == cls:
                    cls_objects.append({key: self.__objects[key]})
            return cls_objects
        return self.__objects

    def save(self):
        """
        Saves all objects in the __objects dictionary to the JSON file.
        """
        with open(self.__file_path, 'w') as f:
            json_objects = {}
            for key, obj in self.__objects.items():
                new_obj = obj.to_dict()
                for okey in new_obj.keys():
                    if isinstance(getattr(obj, okey), datetime):
                        new_obj[okey] = getattr(obj,
                                                okey).strftime(self.__time_f)

                json_objects[key] = new_obj
            json.dump(json_objects, f)

    def add(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj (object): The object to add.
        """
        new_obj = {obj.__class__.__name__ + '.' + obj.id: obj}
        self.__objects.update(new_obj)

    def get(self, cls, oid=None):
        """
        Retrieves an object from the __objects dictionary.

        Args:
            cls (class or str): The class of the object to retrieve,
                                or the class name as a string.
            oid (str, optional): The id of the object to retrieve.
                                Defaults to None.

        Returns:
            object: The retrieved object, or None if not found.
        """

        if isinstance(cls, str) and cls not in self.__classes:
            return None

        if isinstance(cls, str) and oid is None:
            return None

        if isinstance(cls, BaseModel):
            oid = cls.id
            cls = cls.__class__.__name__

        for key in self.__objects.keys():
            cls_name = key.split('.')[0]
            o_id = key.split('.')[1]

            if cls_name == cls and oid == o_id:
                return self.__objects[key]

        return None

    def delete(self, cls, oid=None):
        """
        Deletes an object from the __objects dictionary.

        Args:
            cls (class or str): The class of the object to delete,
                                or the class name as a string.
            oid (str, optional): The id of the object to delete.
                                Defaults to None.
        """
        if isinstance(cls, str) and cls not in self.__classes:
            return None

        if isinstance(cls, str) and oid is None:
            return None

        if isinstance(cls, BaseModel):
            oid = cls.id
            cls = cls.__class__.__name__

        del self.__objects[cls + '.' + oid]
