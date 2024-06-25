# Solved on 02/06/2024
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        n = len(s)
        vowel_count = 0
        for i in range(min(k, n)):
            if s[i] in vowels: vowel_count += 1
        max_count = vowel_count
        for i in range(k, n):
            vowel_count += (s[i] in vowels) - (s[i-k] in vowels)
            max_count = max(max_count, vowel_count)
        return max_count
