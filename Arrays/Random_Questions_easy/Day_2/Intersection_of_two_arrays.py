"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
be unique and you may return the result in any order.

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""
nums_1 = list(map(int,input().split()))
nums_2 = list(map(int,input().split()))
answer = []
nums_1_len = len(nums_1)
nums_2_len = len(nums_2)
if nums_2_len <= nums_1_len:
    for i in range(nums_2_len):
        if (nums_2[i] in nums_1) and (nums_2[i] not in answer):
            answer.append(nums_2[i])
else:
    for i in range(nums_1_len):
        if (nums_1[i] in nums_2) and (nums_1[i] not in answer):
            answer.append(nums_1[i])
print(answer)


