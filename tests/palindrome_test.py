import unittest

from python.basic.palindrome import Palindrome


class PalindromeTest(unittest.TestCase):

    def test_str_to_list(self):
        ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
        # self.mock.str_to_list()
        print(f'test_str_to_list : {ls}')

    def test_isPalindrome(self) ->bool:
        ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
        dict = {"RESULT": True for i in ls if ls.pop(0) != ls.pop()}
        print(f'test_isPalindrome: {dict["RESULT"]}')
        # self.mock.isPalindrome()

if __name__ == '__main__':
    unittest.main()