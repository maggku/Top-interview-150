"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2



Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    The input is generated such that a majority element will exist in the array.


Follow-up: Could you solve the problem in linear time and in O(1) space?

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # use a dictionary to count numbers

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # check witch is a majority element

        for num, count in counts.items():
            if count > len(nums) // 2:
                return num

assert Solution().majorityElement([3,2,3]) == 3
assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2

"""
There's a classic trick for this called the Boyer-Moore Voting Algorithm. Here's the intuition before I show code:
Imagine you keep a candidate and a count. You walk through the array once:

If your count is 0, you pick the current number as your new candidate.
If the current number matches your candidate, you count += 1.
If it doesn't match, you count -= 1.

The idea: think of it like a "tug of war" — the majority number effectively cancels out one occurrence of every other number it's paired against, and because it appears more than half the time, it can never fully get cancelled out. It'll always survive as the candidate by the end.
Want to try tracing this through [2,2,1,1,1,2,2] by hand first (tracking candidate and count at each step) to see if you believe it survives? That's usually the best way to get the "aha" moment before coding it."""



# Use the Boyer-Moore Voting Algorithm to find the answer

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = None
        count = 0

        for i in range(0, len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count += 1
            else:
                count -=1
        return candidate


assert Solution().majorityElement([3,2,3]) == 3
assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2