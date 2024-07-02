# Solved on 02/07/2024
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.changes = 0
        self.visited = [False for _ in range(n)]
        # Creating adjecency list for runtime efficiency - wasn't given
        self.adjecency_list = [[] for _ in range(n)]
        for c in connections:
            self.adjecency_list[c[0]].append(c)
            self.adjecency_list[c[1]].append(c)

        def dfs(city):
            self.visited[city] = True
            for road in self.adjecency_list[city]:
                if self.visited[road[0]] and self.visited[road[1]]: continue
                if road[0] == city: 
                    self.changes += 1
                    dfs(road[1])
                else: dfs(road[0])
                
        dfs(0)
        return self.changes
