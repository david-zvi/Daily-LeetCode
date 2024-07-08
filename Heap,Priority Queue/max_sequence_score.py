# Solved on 08/07/2024
#

import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Sort nums1, nums2 pairs by nums2 value
        pairs = sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True)
        
        res = 0
        prefix_sum = 0
        heap = []
        for n1, n2 in pairs:
            # Keep prefix sum of pairs and add n1's to min heap
            prefix_sum += n1
            heapq.heappush(heap, n1)
            # If heap has k elements in it check if prefix sum times the current n2
            # is greater than previous, if yes update the result (current n2 will
            # always be the smallest we got to because we sorted by the values in
            # nums2)
            if len(heap) == k:
                res = max(res, prefix_sum*n2)
                # Subtract smallest n1 - if the result grew we subtract an n1 that
                # has an n2 value which makes the result smaller, and if it didn't
                # we subtract the n1 we just added
                prefix_sum -= heapq.heappop(heap)
        return res

