"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
"""Example:
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
"""

nums = list(map(int, input("Enter array1").split(",")))
val = int(input("enter the value you want to delete"))
num_len = len(nums)
i = 0
j = num_len - 1
k = 0
while j > i:
    if nums[j] == val:
        j -= 1
        continue
    if nums[i] == val:
        nums[i] = nums[j]
        nums[j] = val
        i += 1
for index in range(num_len):
    if nums[index] == val:
        k = index
        break
    elif val not in nums:
        k = num_len
print(k)