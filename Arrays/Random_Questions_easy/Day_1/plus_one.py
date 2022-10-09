"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Input: digits = [9]
Output: [1,0]
"""
digits = list(map(int, input().split()))
num = ''
for digit in digits:
    num += str(digit)
ans = str(int(num)+1)
arr = []
for digit in ans:
    arr.append(int(digit))
print(arr)

