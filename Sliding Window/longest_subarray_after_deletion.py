# Solved on 01/06/2024
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        before, after = 0, 0
        m = float("-inf")
        i = 0
        while i < n:
            j = i
            while j < n and nums[j]:
                after += 1
                j += 1
            m = max(m, before + after)
            if j >= n: break
            i = j + 1
            before = after
            after = 0
        return n-1 if i == 0 else m
