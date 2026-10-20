#class StringPalindrome:
def is_palindrome(s):

    for i in range(len(s) // 2):
        j = len(s) - 1 - i

        if s[i] != s[j]:
            return False

    return True

    '''def test():
        print("hello test")*/'''


print(is_palindrome("madam"))
#StringPalindrome.test()