import unittest
from datetime import datetime, timedelta
import uuid
from models.reading_log import ReadingLog
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class ReadingLogModelTestCase(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        br_id = str(uuid.uuid4())
        self.brlog = BookReading(br_id=br_id, pages_read=20, hours_read=2)
        self.brlog.add()
        self.brlog.save()

    def tearDown(self):
        # self.file_storage.delete('User', self.user.id)
        pass

    def test_brlog_model_is_instance_of_basemodel(self):
        self.assertTrue(isinstance(self.brlog, BaseModel))

    def test_brlog_model_attributes_existence(self):
        self.assertTrue(hasattr(self.brlog, 'br_id'))
        self.assertTrue(hasattr(self.brlog, 'pages_read'))
        self.assertTrue(hasattr(self.brlog, 'hours_read'))

    def test_brlog_model_attributes(self):
        self.assertEqual(self.brlog.br_id, self.br_id)
        self.assertEqual(self.brlog.pages_read, 20)
        self.assertEqual(self.brlog.hours_read, 2)

    def test_brlog_model_attrib_types(self):
        self.assertTrue(isinstance(uuid.UUID(self.brlog.br_id, uuid.UUID))
        self.assertTrue(isinstance(self.brlog.pages_read, int))
        self.assertTrue(isinstance(self.brlog.hours_read, int))
        self.assertTrue(isinstance(self.brlog.created_at, datetime))
        self.assertTrue(isinstance(self.brlog.updated_at, datetime))
        self.assertTrue(isinstance(uuid.UUID(self.brlog.id), uuid.UUID))

        # check for invalid id
        self.brlog.id = '4343'
        with self.assertRaises(ValueError):
            uuid.UUID(self.brlog.id)

    def test_brlog_model_modification(self):
        old_br_id = self.brlog.br_id
        self.brlog.br_id = str(uuid.uuid4())
        self.brlog.add()
        self.brlog.save()

        # get the brlog
        modf_brlog = self.file_storage.get('BookReading', self.brlog.id)
        self.assertNotEqual(old_br_id, modf_brlog.br_id)

    def test_brlog_model_save_and_load(self):
        loaded_user = self.file_storage.get('User', self.user.id)
        self.assertIsNotNone(loaded_user)
        self.assertEqual(loaded_user.username, 'testuser')
        self.assertEqual(loaded_user.first_name, 'Test')
        self.assertEqual(loaded_user.age, 25)


    def test_brlog_model_created_and_updated_at(self):
        self.assertIsNotNone(self.brlog.created_at)
        self.assertIsNotNone(self.brlog.updated_at)

        # Update user and check updated_at
        self.user.first_name = 'Updated'
        self.user.add()
        self.file_storage.save()
        self.assertIsNotNone(self.brlog.updated_at)
        self.assertNotEqual(self.brlog.created_at, self.user.updated_at)

    def test_brlog_model_to_dict(self):
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['username'], 'testuser')
        self.assertEqual(user_dict['first_name'], 'Test')
        self.assertEqual(user_dict['age'], 25)
        self.assertEqual(user_dict['created_at'].strftime(time_format), self.user.created_at.strftime(time_format))
        self.assertEqual(user_dict['updated_at'].strftime(time_format), self.user.updated_at.strftime(time_format))

    def test_brlog_model_delete(self):
        key = 'User' + '.' + self.user.id
        self.user.delete()
        self.assertFalse(key in self.file_storage.all())

    def test_brlog_model_str(self):
        user_str = str(self.brlog.
        self.assertIn("'username': 'testuser'", user_str)

if __name__ == '__main__':
    unittest.main()
