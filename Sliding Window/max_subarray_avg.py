# Solved on 01/06/2024
# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        s = sum(nums[:k])
        m = float("-inf")
        for i in range(n-k+1):
            avg = s/k
            m = max(m, avg)
            s -= nums[i]
            if i+k < n: s += nums[i+k]
        return m
