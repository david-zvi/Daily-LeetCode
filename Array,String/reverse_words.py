# Solved on 22/05/2024
# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.strip().split()[::-1])
