# Solved on 11/07/2024
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        pairs = []
        # Sort potions
        potions.sort()

        for i in range(n):
            success_floor = success/spells[i]
            # Binary search to find minimal index j where spells[i]*potions[j]
            j = bisect_left(potions, success_floor)
            pairs.append(m-j)

        return pairs
