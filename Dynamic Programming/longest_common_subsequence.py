# Solved on 21/07/2024
# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Length of longest common subsequence in text1, text2 till (not including) indices i,j, where at indices m/n the subsequence is the entire text
        length_till = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]: length_till[i][j] = length_till[i-1][j-1] + 1
                else: length_till[i][j] = max(length_till[i-1][j], length_till[i][j-1])
        return length_till[m][n]
