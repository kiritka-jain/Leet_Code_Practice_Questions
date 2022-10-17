"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Input: n = 2
Output: false

"""
n = int(input())
square_digits_sum = [n]
flag = True
while n != 1:
    digits_sum = 0
    for digit in str(n):
        digits_sum+= int(digit)*int(digit)
        n = digits_sum
    if n not in square_digits_sum:
        square_digits_sum.append(n)
    else:
        flag =False
        break
if flag:
    print(True)
else:
    print(False)

