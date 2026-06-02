#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for testing the function max integer"""

    def test_ordered_list(self):

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):

        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):

        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_empty_list(self):

        self.assertEqual(max_integer([]), None)

    def test_one_element(self):

        self.assertEqual(max_integer([7]), 7)

    def test_only_negatives(self):

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, -2, 12, 4]), 12)


# Ceci permet d'exécuter les tests si on lance le fichier directement
if __name__ == '__main__':
    unittest.main()
