# Solved on 13/07/2024
# https://leetcode.com/problems/koko-eating-bananas/

from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = (l+r)//2
            hours = 0
            for pile in piles: hours += ceil(pile/k)
            if hours <= h: r = k
            else: l = k + 1
        return l
