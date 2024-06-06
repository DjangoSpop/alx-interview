#!/usr/bin/python3
import unittest
from . import makeChange

class TestMakeChange(unittest.TestCase):
    def setUp(self):
        self.func = makeChange

    def test_zero_total(self):
        self.assertEqual(self.func([1, 2, 3], 0), 0)

    def test_negative_total(self):
        self.assertEqual(self.func([1, 2, 3], -5), 0)

    def test_unreachable_total(self):
        self.assertEqual(self.func([2, 4, 5], 3), -1)

    def test_single_coin(self):
        self.assertEqual(self.func([1, 2, 3], 2), 1)

    def test_multiple_coins(self):
        self.assertEqual(self.func([1, 2, 5], 11), 3)

    def test_zero_coin(self):
        self.assertEqual(self.func([0, 2, 3], 4), -1)

if __name__ == '__main__':
    unittest.main()