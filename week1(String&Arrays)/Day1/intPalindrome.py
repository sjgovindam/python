def intPlalindrome(num):

    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num//10
    return original_num == reversed_num
print(intPlalindrome(124))  # True