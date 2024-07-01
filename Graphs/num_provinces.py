# Solved on 01/07/2024
# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.provinces = 0
        # A city is always connected to itself, i'll use isConnected[city][city]
        # as a tracker for if we visited city to save on memory. Need to change them
        # to false.
        for city in range(n): isConnected[city][city] = False

        def dfs(city):
            # If city was already visited return
            if isConnected[city][city]: return
            isConnected[city][city] = True
            for other_city in range(n): 
                if isConnected[city][other_city]: dfs(other_city)

        for city in range(n):
            if isConnected[city][city]: continue
            self.provinces += 1
            dfs(city)
        return self.provinces
