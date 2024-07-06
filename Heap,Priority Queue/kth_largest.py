# Solved on 06/07/2024
# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, n): heapq.heappushpop(heap, nums[i])
        return heap[0]
