#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        max = __import__('6-max_integer').__doc__
        self.assertTrue(len(max) > 1)

    def test_docstring(self):
        """Tests for funstion docstring"""
        docs = max_integer.__doc__
        self.assertTrue(len(docs) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        emp = []
        self.assertIsNone(max_integer(emp))

    def test_not_args(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""
        oe = [1]
        self.assertEqual(max_integer(oe), 1)

    def test_pos_end(self):
        """Tests for all positive with max at end"""
        pe = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(pe), 50)

    def test_pos_mid(self):
        """Tests for all positive with max in middle"""
        pm = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(pm), 360)

    def test_pos_begin(self):
        """Tests for all positive with max at beginning"""
        pb = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(pb), 200)

    def test_one_neg(self):
        """Tests for list with one negative number"""
        onn = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(onn), 200)

    def test_all_neg(self):
        """Tests for list with all negative numbers"""
        alln = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(alln), -1)

    def test_None(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()