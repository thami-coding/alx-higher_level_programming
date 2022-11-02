#!/usr/bin/python3

from models.base import Base
import unittest

class TestMethods(unittest.TestCase):
    def test_to_json_string(self):
        base = Base(1)

        json_value = base.to_json_string({'x':1})
        self.assertTrue(isinstance(json_value, str))

        json_value = base.to_json_string(None)
        self.assertTrue(isinstance(json_value, str))

    def test_save_to_file(self):
        list_objs = {'x':1, 'y': 2, 'id': 1, 'width': 5, 'height': 4}
    # checks that list_objs fails when it's not a list or if the list 
    # doesn't contain object intances in it
        with self.assertRaises(TypeError):
            Base.save_to_file(list_objs)

    def test_from_json_string(self):
        value = Base.from_json_string("{'x': 1, 'y': 2, 'id': 1, }")
        self.assertFalse(value, str)

        with self.assertRaises(TypeError):
            json_string = "(1, 2, 3, 4, 5)"
            Base.from_json_string(json_string)

    def test_create(self):
        dictionary = [1, 2, 3, 4, 5, 6]

        with self.assertRaises(TypeError):
            Base.create(dictionary)

if __name__ == "__main__":
    unittest.main()
