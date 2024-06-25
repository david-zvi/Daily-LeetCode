# Solved on 30/05/2024
# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        largest = 0
        while r > l:
            largest = max(largest, min(height[l], height[r])*(r-l))
            if height[l] > height[r]: r -= 1
            else: l += 1
        return largest
