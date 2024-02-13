#!/usr/bin/python3
'''
Defines unittests for rectangle.
'''

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_instance(self):
        # Test creating an instance of Rectangle
        r = Rectangle(5, 10)
        self.assertIsInstance(r, Rectangle)

    def test_rectangle_attributes(self):
        # Test attributes of Rectangle instance
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_rectangle_area(self):
        # Test calculating area of Rectangle
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_rectangle_update(self):
        # Test updating attributes of Rectangle
        r = Rectangle(5, 10)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_rectangle_to_dictionary(self):
        # Test converting Rectangle to dictionary
        r = Rectangle(5, 10)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, {
                'id': 1, 'width': 5, 'height': 10, 'x': 0, 'y': 0})


if __name__ == '__main__':
    unittest.main()
