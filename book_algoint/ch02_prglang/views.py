from icecream import ic

from book_algoint.ch02_prglang.models import OneToTen

if __name__ == '__main__':
    a = OneToTen()
    ic(a.one_to_ten_sum_1())
    ic(a.one_to_ten_sum_2())
    ic(a.one_to_ten_sum_3())