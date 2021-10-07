class TestPalindrome(unittest.TestCase):
    def test_str_to_list(self):
        inst=Palindrome()
        inst.input_string="when will i be free from IBS"
        res=inst.isPalindrome()
        print(res)
        # ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
        # print(f'test_str_to_list : {ls}')

    # def test_isPalindrome(self) -> bool:
    #     ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
    #     dict = {"RESULT": True for i in ls if ls.pop(0) != ls.pop()}
    #     print(f'test_isPalindrome: {dict["RESULT"]}')
        # self.mock.isPalindrome()


    def test_reverse_list(self):
        inst=Palindrome()
        inst.input_string="when will i be free from IBS"
        res=inst.reverse_string()
        print(res)
        # ls = [i for i in 'when will i be free from IBS' if i.isalnum()]
        # print(ls[::-1])
        # self.mock.reverse_list(self.mock.str_to_list(payload))
    #
    # def test_list_to_str(self) -> str:
    #     ls = [i for i in 'when will i be free from IBS' if i.isalnum()]
    #     print(" ".join([i for i in ls]))
