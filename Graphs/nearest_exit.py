# Solved on 04/07/2024
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.m = len(maze)
        self.n = len(maze[0])
        self.exit = -1
        # Will hold distances from the entrance, as well as tell us if a spot was visited if it's value != 0.
        self.distances = [[0 for i in range(self.n)] for j in range(self.m)]
        def bfs(entrance):
            queue = deque(entrance)
            while queue:
                vi, vj = queue.popleft(), queue.popleft()
                if [vi,vj] != entrance and (vi == 0 or vi == self.m-1 or vj == 0 or vj == self.n-1):
                    self.exit = self.distances[vi][vj]
                    return
                # Up
                ui, uj = vi - 1, vj
                if 0 <= ui < self.m and 0 <= uj < self.n and maze[ui][uj] == '.' and not self.distances[ui][uj] and [ui,uj] != entrance:
                    queue.append(ui)
                    queue.append(uj)
                    self.distances[ui][uj] = self.distances[vi][vj] + 1
                # Right
                ui, uj = vi, vj + 1
                if 0 <= ui < self.m and 0 <= uj < self.n and maze[ui][uj] == '.' and not self.distances[ui][uj] and [ui,uj] != entrance:
                    queue.append(ui)
                    queue.append(uj)
                    self.distances[ui][uj] = self.distances[vi][vj] + 1
                # Down
                ui, uj = vi + 1, vj
                if 0 <= ui < self.m and 0 <= uj < self.n and maze[ui][uj] == '.' and not self.distances[ui][uj] and [ui,uj] != entrance:
                    queue.append(ui)
                    queue.append(uj)
                    self.distances[ui][uj] = self.distances[vi][vj] + 1
                # Left
                ui, uj = vi, vj - 1
                if 0 <= ui < self.m and 0 <= uj < self.n and maze[ui][uj] == '.' and not self.distances[ui][uj] and [ui,uj] != entrance:
                    queue.append(ui)
                    queue.append(uj)
                    self.distances[ui][uj] = self.distances[vi][vj] + 1
        bfs(entrance)
        return self.exit
