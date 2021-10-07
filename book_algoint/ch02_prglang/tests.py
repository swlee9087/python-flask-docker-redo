import unittest

# import sys
# sys.path.append('/admin/sorting')


# Create your tests here.
from book_algoint.ch02_prglang.models import MySum


class TestMySum(unittest.TestCase):
    # ott = OneToTen()

    def test_one_to_ten_sum_1(self):
        ott = MySum()
        ott.start_number = 1
        ott.end_number = 11
        res = ott.one_to_ten_sum_2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)


if __name__ == '__main__':
    unittest.main()
