from os import environ, getenv
from models.user import User
from models.book import Book
from models.book_reading import BookReading
from models.reading_log import ReadingLog
from models.bookmark_book import BookmarkBook
from models.favourite_book import FavouriteBook
from models.friend import Friend
from models.friend_request import FriendRequest
from models.badge import Badge

if environ['MELV_TYPE_STORAGE'] == 'db':
    # storage type is database storage
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    # storage type is file storage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.load()
