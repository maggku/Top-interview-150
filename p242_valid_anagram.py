"""
Easy
Topics
premium lock iconCompanies

Given two strings s and t, return true if t is an of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.



Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for l in s:
            s_dict[l] = s_dict.get(l, 0) + 1
        for l in t:
            t_dict[l] = t_dict.get(l, 0) + 1

        return s_dict == t_dict
