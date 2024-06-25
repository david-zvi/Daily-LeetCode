# Solved on 04/06/2024
# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
    
    def mergesort(self, nums):
        n = len(nums)
        if n == 1: return nums
        mid = n//2
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        res = []
        nl, nr = len(left), len(right)
        i, j = 0, 0
        while i < nl or j < nr:
            if i < nl and j < nr:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            elif i < nl:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        return res
