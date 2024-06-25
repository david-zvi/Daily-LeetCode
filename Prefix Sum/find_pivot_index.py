# Solved on 06/06/2024
# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum, r_sum = 0, sum(nums) - nums[0]
        n = len(nums)
        for i in range(n):
            if l_sum == r_sum: return i
            l_sum += nums[i]
            if i < n - 1: r_sum -= nums[i+1]
        return -1
