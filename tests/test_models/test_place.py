#!/usr/bin/python3
"""
Contains place test
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test class that tests the Place class
    """

    def setUp(self):
        """
        test instance of class
        """
        obj = Place()
        obj.name = "home"

    def test_attributes(self):
        """
        Docs
        """
        self.assertIsInstance(obj, Place, "")
        self.assertIs(obj.name, "home")


if __name__ == '__main__':
    unittest.main()
