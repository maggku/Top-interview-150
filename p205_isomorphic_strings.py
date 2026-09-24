"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t, t_to_s = {}, {}

        for a, b in zip(s, t):
            if a in s_to_t and s_to_t[a] != b:
                return False
            elif b in t_to_s and t_to_s[b] != a:
                return False
            else:
                s_to_t[a] = b
                t_to_s[b] = a

        return True