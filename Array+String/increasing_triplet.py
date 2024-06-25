# Solved on 26/05/2024
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float('inf'), float('inf')
        for third in nums:
            if second < third: return True
            if third <= first: first = third
            else: second = third
        return False
