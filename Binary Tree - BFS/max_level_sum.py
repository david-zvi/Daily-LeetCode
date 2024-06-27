# Solved on 27/06/2024
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        self.min_level = 0
        self.queue = deque()
        def bfs(root):
            if not root: return
            level_count = 1 # How many nodes are left on the current tree level
            next_level = 0 # How many nodes will be on the next tree level
            cur_level = 1
            cur_sum = 0
            self.queue.append(root)
            while self.queue:
                v = self.queue.popleft()
                if v.right:
                    self.queue.append(v.right)
                    next_level += 1
                if v.left:
                    self.queue.append(v.left)
                    next_level += 1
                cur_sum += v.val
                level_count -= 1
                if level_count == 0:
                    if cur_sum > self.max_sum:
                        self.max_sum = cur_sum
                        self.min_level = cur_level
                    cur_level += 1
                    cur_sum = 0
                    level_count = next_level
                    next_level = 0
        bfs(root)
        return self.min_level
