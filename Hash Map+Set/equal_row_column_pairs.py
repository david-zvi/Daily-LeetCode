# Solved on 10/06/2024
# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = dict()
        for i in range(n):
            row = tuple(grid[i])
            if row in rows: rows[row] += 1
            else: rows[row] = 1
        pairs = 0
        for j in range(n):
            col = tuple([grid[i][j] for i in range(n)])
            if col in rows: pairs += rows[col]
        return pairs
