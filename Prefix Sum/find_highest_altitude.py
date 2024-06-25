# Solved on 01/06/2024
# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur, m = 0, 0
        for altitude in gain:
            cur += altitude
            m = max(m, cur)
        return m
