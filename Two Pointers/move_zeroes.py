# Solved on 28/05/2024
# https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeros = 0
        num_index = 0
        for i in range(n):
            if nums[i] == 0: zeros += 1
            else:
                nums[num_index] = nums[i]
                num_index += 1
        for i in range(zeros):
            nums[n-1-i] = 0
