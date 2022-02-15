"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
"""Example:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

nums = list(map(int, input("Enter array1").split(",")))
num_len = len(nums)
i = 0
j = 1
max_val = nums[0]
while j < (num_len):
    if nums[j] == max_val:
        j += 1
    elif nums[j] > max_val:
        max_val = nums[j]
        i += 1
        nums[i] = max_val
        if j < num_len:
            j += 1
new_len = len(nums[:i+1])
print(nums,new_len)
