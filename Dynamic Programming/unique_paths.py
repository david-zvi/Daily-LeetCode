# Solved on 20/07/2024
# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = [[1 for j in range(n)] for i in range(m)]
        # Iterate over every row. For each 0 < i < m and 0 < j < n there are the sum of the paths to i,j-1 and to
        # i-1,j paths, and for any other i < m and j < n combination there is exactly one path.
        for i in range(1, m):
            for j in range(1, n):
                num_paths[i][j] = num_paths[i][j-1] + num_paths[i-1][j]
        return num_paths[-1][-1]
