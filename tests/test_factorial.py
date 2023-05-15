import unittest

from examples.factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_factorial_oz_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-5)