#!/usr/bin/python3
"""
Defines a database engine
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.book import Book
from models.book_reading import BookReading
from models.book_review import BookReview
from models.bookmark_book import BookmarkBook
from models.reading_log import ReadingLog
from models.friend import Friend
from models.friend_request import FriendRequest
from models.badge import Badge
from models.favourite_book import FavouriteBook
from models.recommend_book import RecommendBook
from sqlalchemy import create_engine, desc, asc, text
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from os import getenv


class DBStorage:
    """A database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("MELV_MYSQL_USER")
        passwd = getenv("MELV_MYSQL_PWD")
        db = getenv("MELV_MYSQL_DB")
        host = getenv("MELV_MYSQL_HOST")
        env = getenv("MELV_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        self.all_class_models = {'Book': Book, 'BookReading': BookReading,
                            'ReadingLog': ReadingLog, 'User': User,
                            'BookReview': BookReview, 'BookmarkBook': BookmarkBook,
                            'Badge': Badge, 'Friend': Friend,
                            'FriendRequest': FriendRequest}

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session) all
        objects depending of the class name (argument cls)

        Return:
            dictionary of objects
        """

        objects = {}
        all_class_models = {'Book': Book, 'BookReading': BookReading,
                            'ReadingLog': ReadingLog, 'User': User,
                            'BookReview': BookReview, 'BookMarkBook': BookMarkBook,
                            'Badge': Badge, 'Friend': Friend,
                            'FriendRequest': FriendRequest}

        if cls:
            for row in self.__session.query(cls).all():
                # create an object in the format <class-name>.<object-id>
                objects.update({'{}.{}'.
                                format(type(cls).__name__, row.id,): row})
        else:
            for key, val in all_class_models.items():
                for row in self.__session.query(val):
                    objects.update({f'{type(row).__name__}.{row.id}': row})

        return objects

    def add(self, obj):
        """
        adds' a new model to the database
        """
        self.__session.add(obj)

    def save(self):
        """
        save changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete a model from the database
        """
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """
        create all the schemas of the model to the database and initialize
        the session
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        """
        release all the resources held by the session and
        terminate the connection
        """
        self.__session.close()

    def get(self, cls, o_id):
        if cls in self.all_class_models.keys():
            model = self.all_class_models[cls]
            return self.__session.query(model).get(o_id)

    def filter(self, cls, prop, val):
        if cls in self.all_class_models.keys():
            model = self.all_class_models[cls]
            print(cls + '.' + prop)
            return self.__session.query(model).filter(Friend.user_id == val).all()

    def readingOnProgress(self, obj):
        model = self.all_class_models['BookReading']
        result = self.__session.query(model).filter(model.user_id == obj.id, model.status.like('%on progress%')).order_by(desc(model.created_at))
        return result

    def badge_by_type(self, btype):
        model = self.all_class_models['Badge']
        badge = self.__session.query(model).filter(model.btype.like('%'+btype+'%')).first()
        return badge

    def search_books_read(self, user_id, query):
        filter_text = ''
        params_val = {}

        # we do this to prevent sql injection attack and also filter based on
        # multiple criteria
        if isinstance(query, dict):
            if 'title' in query.keys():
                filter_text += 'title LIKE :title'
                params_val['title'] = f"%{query['title']}%"
            if 'genere' in query.keys():
                filter_text += ' AND genere LIKE :genere'
                params_val['genere'] = f"%{query['genere']}%"
        
        result = self.__session.query(BookReading.user_id, Book.title, Book.genere).\
                               join(Book).filter(text(filter_text).params(**params_val)).all()
# filter(BookReading.user_id == user_id).all()
        return result
