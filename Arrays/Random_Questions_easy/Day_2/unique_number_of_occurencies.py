"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique,
or false otherwise.
eg:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

"""
arr = list(map(int,input().split()))
nums_dict = {}
for num in arr:
    if num not in nums_dict:
        nums_dict[num] = 1
    else:
        nums_dict[num] += 1
if (len(nums_dict)) != (len(set(nums_dict.values()))):
    print(False)
else:
    print(True)
