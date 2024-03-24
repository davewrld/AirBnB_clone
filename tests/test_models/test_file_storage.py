#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        Sets up a temporary file for testing.
        """
        self.test_file = "test_file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """
        Removes the temporary file after testing.
        """
        import os
        if os.path.exists(self.__file_path):
            os.remove(self.__file_path)

    def test_all_empty(self):
        """
        Tests that all() returns an empty dictionary
        when no objects are stored.
        """
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

    def test_all(self):
        """
        Test all() returns objects
        """
        self.assertIsInstance(self.file_storage.all(), dict)
        self.assertEqual(len(self.file_storage.all()), 0)

    def test_new(self):
        """
        Tests that new() stores an object
        """
        new_object = BaseModel()
        self.file_storage.new(new_object)
        self.assertEqual(len(self.file_storage.all()), 1)

    def test_save_and_reload(self):
        """
        Tests that save() serializes objects and reload() deserializes them.
        """
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()

        self.assertTrue(os.path.exists(self.__file_path))


if __name__ == "__main__":
    unittest.main()
