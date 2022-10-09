"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [4,1,2,1,2]
Output: 4

"""
nums = list(map(int,input().split()))
nums_dict = {}
for num in nums:
    if num not in nums_dict:
        nums_dict[num] = 1
    else:
        nums_dict[num] +=1
for num,val in nums_dict.items():
    if val == 1:
        print(num)