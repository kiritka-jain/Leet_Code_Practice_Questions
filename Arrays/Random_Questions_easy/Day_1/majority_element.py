"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from collections import OrderedDict

nums = list(map(int, input().split()))
nums_dict = {}
for num in nums:
    if num not in nums_dict:
        nums_dict[num] = 1
    else:
        nums_dict[num] += 1
print(sorted(nums_dict.items(), key=lambda t: t[1])[-1][0])
