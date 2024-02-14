#!/usr/bin/python3
"""test base module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
import io


class baseClassTest(unittest.TestCase):
    """Test base class"""

    def setUp(self):
        """function that passed to all tests"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test to inter id"""
        ins = Base(3)
        self.assertEqual((ins.id), 3)

    def test_defult_id(self):
        """Test the default id one"""
        ins = Base()
        self.assertEqual((ins.id), 1)

    def test_id_nb(self):
        """Test to call empty Base multiple time"""
        ins1 = Base()
        ins2 = Base()
        ins3 = Base()
        self.assertEqual((ins1.id), 1)
        self.assertEqual((ins2.id), 2)
        self.assertEqual((ins3.id), 3)

    def test_id_mix(self):
        """Test inter diff id's"""
        ins = Base()
        ins1 = Base(11)
        ins2 = Base()
        self.assertEqual((ins.id), 1)
        self.assertEqual((ins1.id), 11)
        self.assertEqual((ins2.id), 2)

    def test_string_id(self):
        """Test to inter string"""
        ins = Base("1")
        self.assertEqual((ins.id), "1")

    def test_two_args_id(self):
        """Test enter two argument to Base class"""
        with self.assertRaises(TypeError):
            ins = Base(1, 1)

    def test_access_to_priv(self):
        """Test access to private attributes"""
        ins = Base()
        with self.assertRaises(AttributeError):
            ins.__nb_objects

    def test_save_to_file_1(self):
        """Test JSON file"""
        Square.save_to_file(None)
        res = "[]"
        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual(content, res)

    def test_save_to_file_2(self):
        """Test JSON file"""
        Rectangle.save_to_file(None)
        res = "[]"
        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual(content, res)

if __name__ == "__main__":
    unittest.main()