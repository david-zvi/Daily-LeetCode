# Solved on 25/06/2024
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # LCA will be node where p is on one side and q on the other.
        self.p_path = []
        self.q_path = []
        self.found_p = False
        self.found_q = False
        def dfs(root):
            if not root: return
            if not self.found_p: 
                self.p_path.append(root)
                if root.val == p.val: self.found_p = True
            if not self.found_q: 
                self.q_path.append(root)
                if root.val == q.val: self.found_q = True
            dfs(root.left)
            dfs(root.right)
            if not self.found_p: self.p_path.pop()
            if not self.found_q: self.q_path.pop()
        dfs(root)
        lca_index = 0
        # LCA is in both arrays and all TreeNodes up to and including that index
        # are the same, so we are guaranteed to return in the loop.
        p_len, q_len = len(self.p_path), len(self.q_path)
        while True:
            if lca_index >= p_len or lca_index >= q_len or\
            self.p_path[lca_index].val != self.q_path[lca_index].val: 
                return self.p_path[lca_index-1]
            lca_index += 1
