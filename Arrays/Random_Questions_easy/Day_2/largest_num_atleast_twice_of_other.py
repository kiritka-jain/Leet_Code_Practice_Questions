"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If
it is, return the index of the largest element, or return -1 otherwise.
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
 """
nums = list(map(int,input().split()))
total_num = len(nums)
max_num = max(nums)
max_num_index = nums.index(max_num)
for i in range(total_num):
    if i != max_num_index and nums[i]*2 > max_num:
        print("-1")
    else:
        print(max_num_index)
