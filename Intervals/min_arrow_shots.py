# Solved on 30/07/2024
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort by x_start
        points.sort(key=lambda x: x[0])
        end = float('-inf')
        arrows = 0
        n = len(points)
        for i in range(n):
            # If the interval overlaps with the current one make end the smaller
            # of the current interval's end and this interval's end
            if points[i][0] <= end: end = min(end, points[i][1])
            else: # Next interval starts after current end
                arrows += 1
                end = points[i][1]
        return arrows
