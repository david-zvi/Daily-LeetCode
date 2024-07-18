# Solved on 18/07/2024
# https://leetcode.com/problems/house-robber/

# O(1) memory solution:
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return max(nums)
        # Max total amount robbable till last 3 houses
        total_rob = [nums[0], nums[1], nums[0]+nums[2]]
        for i in range(3, n):
            next_max = max(total_rob[0], total_rob[1])+nums[i]
            total_rob[0], total_rob[1], total_rob[2] = total_rob[1], total_rob[2], next_max
        return max(total_rob[-1], total_rob[-2])

# O(n) memory solution:
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return max(nums)
        # Max total amount robbable till each house
        total_rob = [nums[0], nums[1], nums[0]+nums[2]]
        for i in range(3, n):
            total_rob.append(max(total_rob[-2], total_rob[-3])+nums[i])
        return max(total_rob[-1], total_rob[-2])
