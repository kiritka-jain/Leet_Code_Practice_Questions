"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
n = int(input())
ways_arr = [0,1,2]


def total_ways(n):
    for i in range(3,n+1):
        ways_arr.append(ways_arr[i-1]+ways_arr[i-2])
    return ways_arr[n]


print(total_ways(n))
