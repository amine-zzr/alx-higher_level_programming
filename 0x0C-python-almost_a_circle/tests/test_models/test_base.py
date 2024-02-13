#!/usr/bin/python3
'''Defines unittests for base'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_instance(self):
        # Test creating an instance of Base
        b = Base()
        self.assertIsInstance(b, Base)

    def test_base_id_increment(self):
        # Test incrementing ID for each new instance
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_manual_id(self):
        # Test creating an instance with a manual ID
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_base_to_json_string_empty_list(self):
        # Test the to_json_string method with an empty list
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_from_json_string_empty_string(self):
        # Test the from_json_string method with an empty string
        obj_list = Base.from_json_string("")
        self.assertEqual(obj_list, [])

    def test_base_from_json_string_non_empty_string(self):
        # Test the from_json_string method with a non-empty string
        json_string = '[{"id": 1}, {"id": 2}]'
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(len(obj_list), 2)
        self.assertEqual(obj_list[0].id, 1)
        self.assertEqual(obj_list[1].id, 2)


if __name__ == '__main__':
    unittest.main()
