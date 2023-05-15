import unittest

from examples.common_elements import find_common_elements


class TestFindCommonElements(unittest.TestCase):

    def test_find_common_elements(self):
        self.assertEqual(find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [3, 4, 5])
        self.assertEqual(find_common_elements([1, 2, 3, 4, 5], [6, 7, 8, 9]), [])
        self.assertEqual(find_common_elements([1, 2, 3], [3, 4, 5]), [3])
        self.assertEqual(find_common_elements([], [1, 2, 3]), [])
        self.assertEqual(find_common_elements([], []), [])


if __name__ == '__main__':
    unittest.main()
