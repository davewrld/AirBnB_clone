#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_id_is_unique(self):
        """
        Test if the generated IDs are unique
        """
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_save_method(self):
        """
        Test save method updates the updated_at.
        """
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertGreater(base_model.update_at, initial_updated_at)

    def test_to_dict(self):
        """
        Test if to_dict method returns the correct dictionary
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertTrue(isinstance(base_model_dict, dict))
        self.assertIn('__class__', base_model_dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    def test_str_method(self):
        """
        Test if str method returns the correct string representation
        """
        base_model = BaseModel()
        base_model_str = str(base_model)
        self.assertTrue(base_model.__class__.__name__ in base_model_str)
        self.assertTrue(base_model.id in base_model_str)
        self.assertTrue(base_model.created_at.isoformat() in base_model_str)
        self.assertTrue(base_model.updated_at.isoformat() in base_model_str)


if __name__ == '__main__':
    unittest.main()
