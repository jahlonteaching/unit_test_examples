import unittest

from examples.reverse_string import reverse_string


class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Hola Mundo"), "odnuM aloH")
        self.assertEqual(reverse_string("1234567890"), "0987654321")
        self.assertEqual(reverse_string("¡Hola, mundo!"), "!odnum ,aloH¡")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")


if __name__ == '__main__':
    unittest.main()
