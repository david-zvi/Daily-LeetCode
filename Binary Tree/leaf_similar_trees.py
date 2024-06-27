# Solved on 21/06/2024
# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, leaf_list = []):
        if not root: return leaf_list
        if not root.left and not root.right: return leaf_list + [root.val]
        return leaf_list + self.helper(root.left, leaf_list) + self.helper(root.right, leaf_list)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True
        elif not root1 or not root2: return False
        return self.helper(root1) == self.helper(root2)
        
