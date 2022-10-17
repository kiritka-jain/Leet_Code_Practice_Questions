"""Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of
these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
Input: nums = [2,1,2]
Output: 5
Input: nums = [1,2,1]
Output: 0

"""
nums = list(map(int, input().split()))
sorted_triangle_sides = sorted(nums)
total = len(sorted_triangle_sides)
perimeter = []
for i in range(total - 1, 0, -1):
    if i-2 >= 0:
        a = sorted_triangle_sides[i]
        b = sorted_triangle_sides[i - 1]
        c = sorted_triangle_sides[i - 2]
        if ((a + b) > c) and ((c + b) > a) and ((a + c) > b):
            perimeter.append(a + b + c)
        else:
            perimeter.append(0)
print(max(perimeter))
