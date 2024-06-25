# Solved on 24/06/2024
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_zz = 0
        def dfs(root, last, depth):
            if not root: return
            self.max_zz = max(self.max_zz, depth)
            dfs(root.right, 'r', depth+1 if last != 'r' else 1)
            dfs(root.left, 'l', depth+1 if last != 'l' else 1)
        dfs(root, '', 0)
        return self.max_zz
