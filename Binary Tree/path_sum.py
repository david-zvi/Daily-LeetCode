# Solved on 23/06/2024
# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # self.target_sum = targetSum
        self.prefix_sums = defaultdict(int)
        self.prefix_sums[0] = 1
        self.cur_sum = 0
        self.paths = 0
        def dfs(root):
            if not root: return
            self.cur_sum += root.val
            self.paths += self.prefix_sums[self.cur_sum-targetSum]
            self.prefix_sums[self.cur_sum] += 1
            dfs(root.right)
            dfs(root.left)
            self.prefix_sums[self.cur_sum] -= 1
            self.cur_sum -= root.val
        dfs(root)
        return self.paths
