# Solved on 25/04/2024
# https://leetcode.com/problems/merge-strings-alternately/

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)
        len2 = len(word2)
        merged = ""
        for i in range(min(len1, len2)): merged = merged + word1[i] + word2[i]
        if len1 > len2: 
            for j in range(i+1, len1): merged = merged+word1[j]
        elif len1 < len2: 
            for j in range(i+1, len2): merged = merged+word2[j]
        return merged
