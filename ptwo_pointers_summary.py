"""Two sum II"""
array = [1,2,3,4,5,6,7,8,9]
target = 8


def twosum(array):
    left = 0
    right = len(array)-1

    while left < right:
        if array[left] + array[right] < target:
            left += 1
        elif array[left] + array[right] > target:
            right -= 1
        else:
            return [left + 1, right + 1]

    return []

"""Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

"""

def palindrome(array):
    left = 0
    right = len(array)-1
    while left < right:
        if array[left] == array[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


"""
Container with most water. problem 11

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        best = 0
        while left < right:
            h = min(height[left], height[right])
            best = max(best, h * (right - left))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return best


