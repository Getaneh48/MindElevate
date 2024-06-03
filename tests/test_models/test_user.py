import unittest
from datetime import datetime, timedelta
import uuid
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        self.user = User(username='testuser', password='password', first_name='Test', last_name='User', age=25, sex='Male', picture='test.jpg')
        self.user.add()
        self.user.save()

    def tearDown(self):
        # self.file_storage.delete('User', self.user.id)
        pass

    def test_user_model_is_instance_of_basemodel(self):
        self.assertTrue(isinstance(self.user, BaseModel))

    def test_user_model_attributes_existence(self):
        self.assertTrue(hasattr(self.user, 'username'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'age'))
        self.assertTrue(hasattr(self.user, 'sex'))
        self.assertTrue(hasattr(self.user, 'picture'))
        self.assertTrue(hasattr(self.user, 'book_genere_prefs'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'id'))

    def test_user_model_attributes(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, 'password')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.age, 25)
        self.assertEqual(self.user.sex, 'Male')
        self.assertEqual(self.user.picture, 'test.jpg')
        self.assertEqual(self.user.book_genere_prefs, [])

    def test_user_model_attrib_types(self):
        self.assertTrue(isinstance(self.user.book_genere_prefs, list))
        self.assertTrue(isinstance(self.user.created_at, datetime))
        self.assertTrue(isinstance(self.user.updated_at, datetime))
        self.assertTrue(isinstance(uuid.UUID(self.user.id), uuid.UUID))

        # check for invalid id
        self.user.id = '4343'
        with self.assertRaises(ValueError):
            uuid.UUID(self.user.id)

    def test_user_model_modification(self):
        username = self.user.username
        self.user.username = 'modified_username'
        self.user.add()
        self.user.save()

        # get the user
        modf_user = self.file_storage.get('User', self.user.id)
        self.assertNotEqual(username, modf_user.username)

    def test_user_model_save_and_load(self):
        loaded_user = self.file_storage.get('User', self.user.id)
        self.assertIsNotNone(loaded_user)
        self.assertEqual(loaded_user.username, 'testuser')
        self.assertEqual(loaded_user.first_name, 'Test')
        self.assertEqual(loaded_user.age, 25)


    def test_user_model_created_and_updated_at(self):
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)

        # Update user and check updated_at
        self.user.first_name = 'Updated'
        self.user.add()
        self.file_storage.save()
        self.assertIsNotNone(self.user.updated_at)
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_user_model_to_dict(self):
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['username'], 'testuser')
        self.assertEqual(user_dict['first_name'], 'Test')
        self.assertEqual(user_dict['age'], 25)
        self.assertEqual(user_dict['created_at'].strftime(time_format), self.user.created_at.strftime(time_format))
        self.assertEqual(user_dict['updated_at'].strftime(time_format), self.user.updated_at.strftime(time_format))

    def test_user_model_delete(self):
        key = 'User' + '.' + self.user.id
        self.user.delete()
        self.assertFalse(key in self.file_storage.all())

    def test_user_model_str(self):
        user_str = str(self.user)
        self.assertIn("'username': 'testuser'", user_str)

if __name__ == '__main__':
    unittest.main()
