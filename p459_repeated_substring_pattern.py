"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.



Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:

Input: s = "aba"
Output: false

Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.



Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.

"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # chose a range that is half the lenth
        for length in range(1, n // 2 + 1):
            #check if lenth fiths in n without extras
            if n % length != 0:
                continue
                #build a piece
            piece = s[:length]
            #check if you can build s with multiplying piece with n//lenth
            if piece * (n // length) == s:
                return True

        return False