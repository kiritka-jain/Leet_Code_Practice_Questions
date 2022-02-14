""" insert an element at the end of the array """

arr = list(map(int, input("Enter the array:").split(',')))
arr_len = len(arr)
element_to_insert = int(input("Enter the value you want to insert:"))
arr.insert(arr_len + 1, element_to_insert)
print(arr)

"""insert an element at any position in the array."""

arr = list(map(int, input("Enter the array:").split(',')))
arr_len = len(arr)
element_to_insert = int(input("Enter the value you want to insert:"))
insert_num_at_position = int(input("Enter the position at which you want to insert the value:"))
for i in range(arr_len, insert_num_at_position, -1):
    if i == arr_len:
        arr.insert(i, arr[(i - 1)])
    else:
        arr[i] = arr[i-1]
arr[insert_num_at_position] = element_to_insert
print(arr)

""" ques: Given a fixed-length integer array arr, duplicate each occurrence of zero,
 shifting the remaining elements to the right.
 Eg: Input: arr = [1,0,2,3,0,4,5,0]
 Output: [1,0,0,2,3,0,0,4]"""

arr = list(map(int, input("Enter the array:").split(',')))
arr_len = len(arr)
i = 0
while i < arr_len:
    if arr[i] == 0 and i < arr_len - 1:
        for j in range(arr_len - 1, i + 1, -1):
            arr[j] = arr[j - 1]
        arr[i + 1] = arr[i]
        i += 2
    else:
        i += 1
print(arr)

"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and
 two integers m and n, representing the number of elements in nums1 and nums2 respectively.
 Merge nums1 and nums2 into a single array sorted in non-decreasing order."""
# using a third array
n = int(input())
nums1 = list(map(int, input("Enter array1").split(",")))
m = int(input())
nums2 = list(map(int, input("Enter array2").split(",")))
resultant_array = []
i = 0
j = 0
while i<n and j< m:
    if nums1[i] > nums2[j]:
        resultant_array.append(nums2[j])
        j+=1
    elif nums1[i] < nums2[j]:
        resultant_array.append(nums1[i])
        i+=1
    elif nums1[i] == nums2[j]:
        resultant_array.append(nums1[i])
        resultant_array.append(nums2[j])
        i+=1
        j+=1
if (n-i) !=0:
    for elem in range(i,n):
         resultant_array.append(nums1[elem])
elif (m-j) != 0:
    for elem in range(j,m):
        resultant_array.append(nums2[elem])
nums1 = resultant_array
print(nums1)

"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and
 two integers m and n, representing the number of elements in nums1 and nums2 respectively.
 Merge nums1 and nums2 into a single array sorted in non-decreasing order."""
# without using any third array
i = m - 1
j = n - 1
insert_at = (n + m) - 1
while i >= 0 and j >= 0:
    if nums2[j] >= nums1[i]:
        nums1[insert_at] = nums2[j]
        j -= 1
    else:
        nums1[insert_at] = nums1[i]
        i -= 1
    insert_at -= 1
if j >=0:
    for pos in range(j,-1,-1):
        nums1[insert_at] = nums2[pos]
        if insert_at >0:
            insert_at-=1

print(nums1)
