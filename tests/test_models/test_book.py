import unittest
from datetime import datetime, timedelta
import uuid
from models.book import Book
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class BookModelTestCase(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        self.book = Book()
        self.book.add()
        self.book.save()

    def tearDown(self):
        pass

    def test_book_model_is_instance_of_basemodel(self):
        self.assertTrue(isinstance(self.book, BaseModel))

    def test_book_model_attributes_existence(self):
        self.assertTrue(hasattr(self.book, 'title'))
        self.assertTrue(hasattr(self.book, 'author'))
        self.assertTrue(hasattr(self.book, 'genere'))
        self.assertTrue(hasattr(self.book, 'pub_year'))
        self.assertTrue(hasattr(self.book, 'pages'))
        self.assertTrue(hasattr(self.book, 'cover_image'))
        self.assertTrue(hasattr(self.book, 'id'))
        self.assertTrue(hasattr(self.book, 'created_at'))
        self.assertTrue(hasattr(self.book, 'updated_at'))

    def test_book_model_attributes(self):
        self.assertEqual(self.book.title, '')
        self.assertEqual(self.book.author, '')
        self.assertEqual(self.book.genere, '')
        self.assertEqual(self.book.pub_year, '')
        self.assertEqual(self.book.pages, 0)
        self.assertEqual(self.book.cover_image, '')

    def test_book_model_attrib_types(self):
        self.assertTrue(isinstance(self.book.pages, int))
        self.assertTrue(isinstance(self.book.id, str))
        self.assertTrue(isinstance(self.book.title, str))
        self.assertTrue(isinstance(self.book.author, str))
        self.assertTrue(isinstance(self.book.genere, str))
        self.assertTrue(isinstance(self.book.cover_image, str))
        self.assertTrue(isinstance(self.book.updated_at, datetime))
        self.assertTrue(isinstance(self.book.created_at, datetime))
        self.assertTrue(isinstance(uuid.UUID(self.book.id), uuid.UUID))

        # check for invalid id
        self.book.id = '4343'
        with self.assertRaises(ValueError):
            uuid.UUID(self.book.id)

    def test_book_model_modification(self):
        bookname = self.book.title
        self.book.title = bookname + "modf"
        self.book.add()
        self.book.save()

        # get the book
        modf_book = self.file_storage.get('Book', self.book.id)
        self.assertNotEqual(bookname, modf_book.title)

    def test_book_model_save_and_load(self):
        self.book.title = 'Atomic Habit'
        self.book.author = 'James Clear'
        self.book.add()
        self.book.save()
        loaded_book = self.file_storage.get('Book', self.book.id)
        self.assertIsNotNone(loaded_book)
        self.assertEqual(loaded_book.title, 'Atomic Habit')
        self.assertEqual(loaded_book.author, 'James Clear')

    def test_book_model_created_and_updated_at(self):
        self.assertIsNotNone(self.book.created_at)
        self.assertIsNotNone(self.book.updated_at)

        # Update book and check updated_at
        self.book.add()
        self.file_storage.save()
        self.assertIsNotNone(self.book.updated_at)
        self.assertNotEqual(self.book.created_at, self.book.updated_at)

    def test_book_model_to_dict(self):
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.book.title = 'Atomic Habit'
        self.book.add()
        book_dict = self.book.get().to_dict()
        self.assertEqual(book_dict['title'], 'Atomic Habit')
        self.assertEqual(book_dict['created_at'].strftime(time_format), self.book.created_at.strftime(time_format))
        self.assertEqual(book_dict['updated_at'].strftime(time_format), self.book.updated_at.strftime(time_format))

    def test_book_model_delete(self):
        key = 'Book' + '.' + self.book.id
        self.book.delete()
        self.assertFalse(key in self.file_storage.all())

    def test_book_model_str(self):
        self.book.title = 'Atomic Habit'
        self.book.add()
        book_str = str(self.book)
        self.assertIn("'title': 'Atomic Habit'", book_str)

if __name__ == '__main__':
    unittest.main()
