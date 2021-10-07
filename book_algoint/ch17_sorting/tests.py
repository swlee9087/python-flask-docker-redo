import unittest

from admin.sorting.basic.models_sort import *


class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        inst = Sorting()
        inst.random_arr = [8, 4, 6, 2, 9, 1, 3, 7, 5]
        res = inst.bubble_sort()
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_merge_sort(self):
        arr = Sorting.random_arr = [8, 4, 6, 2, 9, 1, 3, 7, 5]
        arr = Sorting.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quick_sort(self):
        arr = Sorting.random_arr = [8, 4, 6, 2, 9, 1, 3, 7, 5]
        arr = Sorting.quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
