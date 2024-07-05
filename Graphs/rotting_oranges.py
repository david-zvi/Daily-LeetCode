# Solved on 05/07/2024
# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.minutes = 0
        self.fruit_count = 0

        def bfs(queue):
            directions = [(-1,0), (0,1), (1,0), (0,-1)]
            while queue:
                # How many fruits rotted in the previous minute
                prev_rot = len(queue)
                rotted = False
                for _ in range(prev_rot//2):
                    vi, vj = queue.popleft(), queue.popleft()
                    self.fruit_count -= 1
                    for di, dj in directions:
                        ui, uj = vi + di, vj + dj
                        if 0 <= ui < self.m and 0 <= uj < self.n and grid[ui][uj] == 1:
                            rotted = True
                            queue.append(ui)
                            queue.append(uj)
                            grid[ui][uj] = 2
                if rotted: self.minutes += 1
        queue = deque()
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]: self.fruit_count += 1
                if grid[i][j] == 2: queue.extend([i,j])
        bfs(queue)
        return -1 if self.fruit_count else self.minutes
