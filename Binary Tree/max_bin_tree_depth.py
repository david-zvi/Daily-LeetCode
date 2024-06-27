# Solved on 20/06/2024
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthHelper(self, root, depth):
        if not root: return depth
        return max(self.depthHelper(root.left, depth+1), 
                   self.depthHelper(root.right, depth+1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return self.depthHelper(root, 0)
        
