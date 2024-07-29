# Solved on 29/07/2024
# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by ends of intervals
        intervals.sort(key=lambda interval: interval[1])
        erases = 0
        end = float("-inf")
        for interval in intervals:
            # If the next interval (smallest end time) starts when/after the last
            # interval we added ends add it, else remove it
            if interval[0] >= end: end = interval[1]
            else: erases += 1
        return erases
