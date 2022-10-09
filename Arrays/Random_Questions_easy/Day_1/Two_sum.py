"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
eg:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
nums = list(map(int, input().split()))
target = int(input())
num_len = len(nums)
ans = []
# using two for loops

for i in range(num_len):
    for j in range(i+1,num_len):
        if nums[i]+nums[j] == target:
            ans.append(i)
            ans.append(j)

# using one for loop

for i in range(num_len):
    num = target - nums[i]
    if num in nums:
        j = nums.index(num)
        if i != j and (i and j not in ans):
            ans.append(i)
            ans.append(j)
print(ans)
