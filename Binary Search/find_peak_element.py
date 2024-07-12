# Solved on 12/07/2024
# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            # If mid is a peak return it, else change pointer to side that's
            # bigger than mid to point at it/right after it.
            mid = (l+r)//2
            if mid == 0 and nums[mid]>nums[mid+1]: return mid
            elif mid == n-1 and nums[mid-1]<nums[mid]: return mid
            elif nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]: return mid

            if nums[mid] <= nums[mid+1]: l = mid+1
            else: r = mid
        
        return l
