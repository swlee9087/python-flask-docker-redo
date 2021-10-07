from book_algoint.string_tut.models import Palindrome, Reverse

if __name__ == '__main__':
    ls = Palindrome.str_to_list("A man, a plan, a canal: Panama")
    print(ls)
    isPal = Palindrome.isPalindrome(ls)
    print(isPal["result"])

    ls2 = Reverse.str_to_list(input("Input "))
    rev_ls = Reverse.reverse_list(ls2)
    print(Reverse.list_to_str(rev_ls))
