import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +", False)
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -", False)
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *", False)
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /", False)
        self.assertEqual(2, result)
    def test_exponentiation(self):
        result = rpn.calculate("2 2 ^", False)
        self.assertEqual(4, result)