"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""
s = input()
string_to_test = ''
for alphabet in s:
    if alphabet.isalnum():
        string_to_test += alphabet.lower()
# rev_string = string_to_test[::-1]
# if string_to_test == rev_string:
#     print(True)
# else:
#     print(False)

## using two pointer technique

l_pointer = 0
r_pointer = len(string_to_test)-1
flag = True
while l_pointer < r_pointer:
    if string_to_test[l_pointer] == string_to_test[r_pointer]:
        l_pointer +=1
        r_pointer -=1
    else:
        flag = False
        break
if flag:
    print(True)
else:
    print(False)


