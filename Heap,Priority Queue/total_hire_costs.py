# Solved on 09/07/2024
# https://leetcode.com/problems/total-cost-to-hire-k-workers/

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Create heaps for first and last candidates costs in costs
        l_heap, r_heap = [], []
        l, r = 0, len(costs) - 1
        # Flag to know if we iterated over the entire array
        iterated_all = False
        for _ in range(candidates):
            if l >= r: 
                iterated_all = True
                break
            heapq.heappush(l_heap, costs[l])
            heapq.heappush(r_heap, costs[r])
            l += 1
            r -= 1
        # If we iterated on the entire array and l==r (we didn't add the l/r'th cost) add it to the left heap
        if iterated_all and l==r: 
            heapq.heappush(l_heap, costs[l])
            l += 1
        total = 0
        for _ in range(k):
            # Hired all workers
            if not l_heap and not r_heap: break
            # r_heap is empty or both aren't and l min < r min
            if not r_heap or (l_heap and l_heap[0] <= r_heap[0]):
                total += heapq.heappop(l_heap)
                if l <= r: 
                    heapq.heappush(l_heap, costs[l])
                    l += 1
            # l_heap is empty or both aren't and l min >= r min
            else:
                total += heapq.heappop(r_heap)
                if l <= r: 
                    heapq.heappush(r_heap, costs[r])
                    r -= 1
        return total
