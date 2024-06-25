# Solved on 25/05/2024
# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) 
        from_start = [1] * n
        from_end = [1] * n
        for i in range(1,n):
            from_start[i] = from_start[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            from_end[i] = from_end[i+1] * nums[i+1]
        return [from_start[i]*from_end[i] for i in range(n)]
