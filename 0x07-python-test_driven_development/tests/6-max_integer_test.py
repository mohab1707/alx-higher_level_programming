#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_duplicate_elements(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)
        self.assertEqual(max_integer([-2, -2, -2]), -2)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_mixed_list(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([10, -5, 7, -3]), 10)
        self.assertEqual(max_integer([0, -2, -8, -4]), 0)
