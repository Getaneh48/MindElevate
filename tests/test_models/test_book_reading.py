import unittest
from datetime import datetime, timedelta
import uuid
from models.book_reading import BookReading
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class BookReadingModelTestCase(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        self.book_rd = BookReading()
        self.book_rd.add()
        self.book_rd.save()

    def tearDown(self):
        pass

    def test_book_reading_model_is_instance_of_basemodel(self):
        self.assertTrue(isinstance(self.book_rd, BaseModel))

    def test_book_reading_model_attributes_existence(self):
        self.assertTrue(hasattr(self.book_rd, 'user_id'))
        self.assertTrue(hasattr(self.book_rd, 'book_id'))
        self.assertTrue(hasattr(self.book_rd, 'pages_per_day'))
        self.assertTrue(hasattr(self.book_rd, 'hours_per_day'))
        self.assertTrue(hasattr(self.book_rd, 'expected_completion_day'))
        self.assertTrue(hasattr(self.book_rd, 'status'))
        self.assertTrue(hasattr(self.book_rd, 'is_favorite'))
        self.assertTrue(hasattr(self.book_rd, 'friend_visible'))
        self.assertTrue(hasattr(self.book_rd, 'start_date'))
        self.assertTrue(hasattr(self.book_rd, 'id'))
        self.assertTrue(hasattr(self.book_rd, 'created_at'))
        self.assertTrue(hasattr(self.book_rd, 'updated_at'))

    def test_book_reading_model_attributes(self):
        self.assertEqual(self.book_rd.pages_per_day, 0)
        self.assertEqual(self.book_rd.hours_per_day, 0)
        self.assertEqual(self.book_rd.expected_completion_day, 0)
        self.assertEqual(self.book_rd.is_favorite, False)
        self.assertEqual(self.book_rd.friend_visible, False)

    def test_book_reading_model_attrib_types(self):
        self.assertTrue(isinstance(self.book_rd.pages_per_day, int))
        self.assertTrue(isinstance(self.book_rd.hours_per_day, int))
        self.assertTrue(isinstance(self.book_rd.expected_completion_day, int))
        self.assertTrue(isinstance(self.book_rd.status, str))
        self.assertTrue(isinstance(self.book_rd.is_favorite, bool))
        self.assertTrue(isinstance(self.book_rd.friend_visible, bool))
        self.assertTrue(isinstance(self.book_rd.updated_at, datetime))
        self.assertTrue(isinstance(self.book_rd.created_at, datetime))
        self.assertTrue(isinstance(uuid.UUID(self.book_rd.id), uuid.UUID))

        # check for invalid id
        self.book_rd.id = '4343'
        with self.assertRaises(ValueError):
            uuid.UUID(self.book_rd.id)

    def test_book_reading_model_modification(self):
        prev_bid = self.book_rd.book_id
        self.book_rd.book_id = str(uuid.uuid4())
        self.book_rd.add()
        self.book_rd.save()

        # get the book
        modf_book = self.file_storage.get('BookReading', self.book_rd.id)
        self.assertNotEqual(prev_bid, modf_book.book_id)

    def test_book_reading_model_save_and_load(self):
        user_id = str(uuid.uuid4())
        book_id = str(uuid.uuid4())
        self.book_rd.user_id = user_id
        self.book_rd.book_id = book_id
        self.book_rd.add()
        self.book_rd.save()
        loaded_book = self.file_storage.get('BookReading', self.book_rd.id)
        self.assertIsNotNone(loaded_book)
        self.assertEqual(loaded_book.user_id, user_id)
        self.assertEqual(loaded_book.book_id, book_id)

    def test_book_reading_model_created_and_updated_at(self):
        self.assertIsNotNone(self.book_rd.created_at)
        self.assertIsNotNone(self.book_rd.updated_at)

        # Update book and check updated_at
        self.book_rd.add()
        self.file_storage.save()
        self.assertIsNotNone(self.book_rd.updated_at)
        self.assertNotEqual(self.book_rd.created_at, self.book_rd.updated_at)

    def test_book_reading_model_to_dict(self):
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        book_id = str(uuid.uuid4())
        self.book_rd.book_id = book_id
        self.book_rd.add()
        book_dict = self.book_rd.get().to_dict()
        self.assertEqual(book_dict['book_id'], book_id)
        self.assertEqual(book_dict['created_at'].strftime(time_format), self.book_rd.created_at.strftime(time_format))
        self.assertEqual(book_dict['updated_at'].strftime(time_format), self.book_rd.updated_at.strftime(time_format))

    def test_book_reading_model_delete(self):
        key = 'BookReading' + '.' + self.book_rd.id
        self.book_rd.delete()
        self.assertFalse(key in self.file_storage.all())

    def test_book_reading_model_str(self):
        book_id = str(uuid.uuid4())
        self.book_rd.book_id = book_id
        self.book_rd.add()
        book_str = str(self.book_rd)
        self.assertIn(f"'book_id': '{book_id}'", book_str)

if __name__ == '__main__':
    unittest.main()
