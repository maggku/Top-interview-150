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

def solution_two_pointers(nums, t):
    left = 0
    right = len(nums) - 1
    nums.sort()

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == t:
            return True
        elif current_sum > t:
            left += 1
        else:
            right -= 1

    return False




#Greedy

def solution_greedy(nums, t):
    seen = set()
    for num in nums:
        complement = t - num
        if complement in seen:
            return True
        seen.add(num)

    return False

#DP