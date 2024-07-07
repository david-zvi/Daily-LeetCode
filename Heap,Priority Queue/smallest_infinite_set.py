# Solved on 07/07/2024
# https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.smallest = 1

    def popSmallest(self) -> int:
        if self.heap: return heapq.heappop(self.heap)
        self.smallest += 1
        return self.smallest - 1

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.heap:
            heapq.heappush(self.heap, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
