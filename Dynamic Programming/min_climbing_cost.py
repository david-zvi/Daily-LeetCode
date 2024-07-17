# Solved on 17/07/2024
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        before_prev, prev = 0, 0
        n = len(cost)
        for i in range(2, n+1):
            cur_cost = min(cost[i-2] + before_prev, cost[i-1] + prev)
            before_prev, prev = prev, cur_cost
        return prev
