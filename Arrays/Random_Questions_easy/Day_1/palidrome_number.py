"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

"""
# # converting number to string

x = int(input())
num = str(x)
rev_num = num[::-1]
if num == rev_num:
    print("Palidrome")
else:
    print("Not a Palidrome.")

