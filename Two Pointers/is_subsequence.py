# Solved on 29/05/2024
# https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_length = len(s)
        if s_length == 0: return True
        if s_length > len(t): return False
        s_ptr = 0
        for letter in t:
            if letter == s[s_ptr]: s_ptr += 1
            if s_ptr == s_length: return True
        return False
