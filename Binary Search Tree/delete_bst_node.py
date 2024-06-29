# Solved on 29/05/2024
# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        def transplant(node, prev, side):
            # Transplants a node's right child in it's place, making the left child a 
            # decendent of the the right one.
            left, right = node.left, node.right
            if side == 'l': prev.left = right
            elif side == 'r': prev.right = right
            # If side is '' node is root
            temp = right
            while temp.left: temp = temp.left
            temp.left = left

        temp = root
        prev = root
        side = ''
        while temp:
            if temp.val == key:
                right = temp.right
                if not temp.left and not temp.right:
                    if side == 'l': prev.left = None
                    else: prev.right = None
                elif temp.left and not temp.right:
                    if not side: return temp.left
                    if side == 'l': prev.left = temp.left
                    else: prev.right = temp.left
                elif not temp.left and temp.right:
                    if not side: return temp.right
                    if side == 'l': prev.left = temp.right
                    else: prev.right = temp.right
                else: # Both left and right children exist
                    transplant(temp, prev, side)
                # if not side root has val key
                return root if side else right
            else:
                prev = temp
                if temp.val > key: 
                    temp = temp.left
                    side = 'l'
                else: 
                    temp = temp.right
                    side = 'r'
        return root
