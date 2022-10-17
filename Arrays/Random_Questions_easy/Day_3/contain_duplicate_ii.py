"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.

Input: nums = [1,2,3,1], k = 3
Output: true
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""
nums = list(map(int, input().split()))
k = int(input())
nums_len = len(nums)
nums_pos_dict = {}

for i in range(nums_len):
    if nums[i] not in nums_pos_dict.keys():
        nums_pos_dict[nums[i]] = [i]
    else:
        nums_pos_dict[nums[i]].append(i)
distinct_var_pos = []
for val_arr in nums_pos_dict.values():
    if len(val_arr) > 1:
        distinct_var_pos = val_arr
distinct_var_pos_len = len(distinct_var_pos)
answer = []
for i in range(distinct_var_pos_len-1):
    if (i < distinct_var_pos_len) and (distinct_var_pos[i + 1] - distinct_var_pos[i]) <= k:
       answer.append(True)
    else:
        answer.append(False)
print(any(answer))
