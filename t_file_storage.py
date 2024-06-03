import unittest
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.user1 = User(email="test1@example.com", password="test123")
        self.user2 = User(email="test2@example.com", password="test456")

    def test_all(self):
        self.storage.add(self.user1)
        self.storage.add(self.user2)

        # Test all objects
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn(self.user1, all_objects)
        self.assertIn(self.user2, all_objects)

        # Test all objects of a specific class
        user_objects = self.storage.all(User)
        self.assertEqual(len(user_objects), 2)
        self.assertIn(self.user1, user_objects)
        self.assertIn(self.user2, user_objects)

    def test_save(self):
        self.storage.add(self.user1)
        self.storage.save()

        # Check if the file exists
        self.assertTrue(os.path.exists(FileStorage.__file_path))

        # Load the file and verify the objects
        with open(FileStorage.__file_path, 'r') as f:
            objs = json.load(f)
            self.assertEqual(len(objs), 1)
            self.assertIn(self.user1.id, objs)

    def test_add(self):
        self.storage.add(self.user1)

        # Verify that the object is added to the dictionary
        self.assertIn(self.user1.__class__.__name__ + '.' + self.user1.id, self.storage.__objects)

    def test_get(self):
        self.storage.add(self.user1)

        # Get by object instance
        retrieved_user1 = self.storage.get(User, self.user1.id)
        self.assertEqual(retrieved_user1, self.user1)

        # Get by class name and id
        retrieved_user2 = self.storage.get("User", self.user1.id)
        self.assertEqual(retrieved_user2, self.user1)
