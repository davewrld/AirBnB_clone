#!/usr/bin/python3
"""
module containing Review class tests
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test class that tests the Review class
    """

    def setUp(self):
        """
        test instance
        """
        obj = Review()
        obj.text = "good"

    def test_attr(self):
        """
        Docs
        """
        self.assertIsInstance(obj, Review, "")


if __name__ == '__main__':
    unittest.main()
