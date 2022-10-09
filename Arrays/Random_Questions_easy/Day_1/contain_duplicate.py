"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


"""
nums = list(map(int,input().split()))
new_num = set(nums)
new_num_len = len(new_num)
num_len = len(nums)
if new_num_len == num_len:
    print(False)
else:
    print(True)