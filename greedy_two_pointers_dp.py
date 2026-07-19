"""
The probelm:
given an array of integers, does there exist a pair of numbers that add up exackly to a targetT?
Example:
    [2, 7, 4, 1, 9, 5] target T =9 (answer yes, 2+7=9)
"""

# My solution

nums = [2, 7, 4, 1, 9, 5]
t = 9

def solution(nums, t):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == t:
                return True
    return False




#Two pointers

#Greedy

#DP