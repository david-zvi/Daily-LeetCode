# Solved on 22/06/2024
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, m):
        if not root: return 0
        if m <= root.val:
            good_root = 1
            m = root.val
        else: good_root = 0
        return good_root + self.helper(root.left, m) + self.helper(root.right, m)

    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, float("-inf"))
