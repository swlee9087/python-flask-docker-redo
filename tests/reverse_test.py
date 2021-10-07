import unittest

from python.basic.reverse import Reverse


class ReverseTest(unittest.TestCase):
    mock = Reverse()

    def test_str_to_list(self):
        ls =[i for i in 'when will i be free from IBS' if i.isalnum()]
        # self.mock.str_to_list(payload)
        print(f'test_str_to_list : {ls}')

    def test_reverse_list(self):
        ls = [i for i in 'when will i be free from IBS' if i.isalnum()]
        print(ls[::-1])
        # self.mock.reverse_list(self.mock.str_to_list(payload))

    def test_list_to_str(self) -> str:
        ls = [i for i in 'when will i be free from IBS' if i.isalnum()]
        print(" ".join([i for i in ls]))
        # self.mock.list_to_str(self.test_reverse_list(self.test_str_to_list()))

if __name__ == '__main__':
    unittest.main()
