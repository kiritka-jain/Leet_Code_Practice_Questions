"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Input: num = 0
Output: 0
"""

num = int(input())
num_str = str(num)
while len(num_str) > 1:
    total = 0
    for digit in num_str:
        total += int(digit)
    num_str = str(total)
print(int(num_str))

