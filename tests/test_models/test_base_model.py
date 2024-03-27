#!/usr/bin/python3
"""
Test for  BaseModel
""""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test BaseModel class
    """

    def setUp(self):
        """
        BaseModel instance for each test case.
        """
        self.model = BaseModel()

    def test_init_kwargs(self):
        """
        Tests that a new BaseModel instance can be created with specific values
        using keyword arguments (kwargs).
        """
        test_id = "abc123"
        test_created_at_str = "2024-03-27T12:00:00"
        test_updated_at_str = "2023-12-31T23:59:59"
        test_created_at = datetime.fromisoformat(test_created_at_str)
        test_updated_at = datetime.fromisoformat(test_updated_at_str)
        base_model = BaseModel(id=test_id, created_at=test_created_at_str, updated_at=test_updated_at_str)
        self.assertEqual(base_model.id, test_id)
        self.assertEqual(base_model.created_at, test_created_at)
        self.assertEqual(base_model.updated_at, test_updated_at)

    def test_has_attribute(self):
        """
        Test if instance has all attributes
        """
        model = BaseModel()
        model.name = "David"
        model.number = 25
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertTrue(hasattr(model, "name"))
        self.assertTrue(hasattr(model, "number"))

    def test_attribute_type(self):
        """
        Test all attributes types
        """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.id, str)

    def test_save(self):
        """
        Test save method
        """
        model = BaseModel()
        model.save()
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict(self):
        """
        Test if to_dict method returns the correct dictionary
        """
        model = BaseModel()
        model.name = "MyBaseModel"
        output_dict = model.to_dict()
        self.assertIn("id", output_dict)
        self.assertIn("created_at", output_dict)
        self.assertIn("updated_at", output_dict)
        self.assertIn("__class__", output_dict)
        self.assertEqual(output_dict["__class__"], "BaseModel")
        self.assertIsInstance(output_dict["created_at"], str)
        self.assertIsInstance(output_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
