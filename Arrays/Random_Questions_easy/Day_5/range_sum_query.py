"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums. int sumRange(int left, int right) Returns
the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... +
nums[right]).

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

"""
num_array_and_sub_range = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
nums_arr = num_array_and_sub_range[0][0]
sum_output = [None]
# for sub_arr_range in range(1,len(num_array_and_sub_range)):
#     arr = (num_array_and_sub_range[sub_arr_range])
#     start_range = arr[0]
#     end_range = arr[1]+1
#     sub_arr = nums_arr[start_range:end_range]
#     sub_arr_sum = sum(sub_arr)
#     sum_output.append(sub_arr_sum)
# print(sum_output)
total = []
nums_sum = 0
for num in nums_arr:
    nums_sum += num
    total.append(nums_sum)
print(total)
for sub_arr_range in range(1,len(num_array_and_sub_range)):
    arr = (num_array_and_sub_range[sub_arr_range])
    left = arr[0]
    right = arr[1]
    if left == 0:
        sub_arr_sum = total[right]
    else:
        sub_arr_sum = (total[right] - total[left-1])
    sum_output.append(sub_arr_sum)
print(sum_output)


