#!/usr/bin/python3
'''Defines unittests for base'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_instance(self):
        # Test creating an instance of Base
        b = Base()
        self.assertIsInstance(b, Base)

    def test_base_id(self):
        # Test assigning an ID to the Base instance
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_to_json_string(self):
        # Test the to_json_string method
        b = Base()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_from_json_string(self):
        # Test the from_json_string method
        json_string = "[]"
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(obj_list, [])

if __name__ == '__main__':
    unittest.main()
