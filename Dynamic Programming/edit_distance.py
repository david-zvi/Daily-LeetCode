# Solved on 23/07/2024
# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # Number of changes that need to be done for subwords word1[:i],word2[:j]
        # Changes for an empty subword and another subword (empty or not) is the
        # length of the longest subword.
        changes = [[0]*(n+1) for i in range(m+1)]
        for i in range(m+1): changes[i][0] = i
        for j in range(n+1): changes[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                # If the letters are the same no change needs to be made, look at
                # the number of changes needed for the subwords upto the letter
                # before the current one
                if word1[i-1] == word2[j-1]: changes[i][j] = changes[i-1][j-1]
                # If not we can either change the last letter of a word to match
                # the other, or add a letter to the end of a subword
                else: changes[i][j] = \
                    min(changes[i-1][j-1], changes[i-1][j], changes[i][j-1]) + 1
        return changes[m][n]
        
