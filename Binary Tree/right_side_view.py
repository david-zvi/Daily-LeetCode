# Solved on 26/06/2024
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        self.queue = deque()
        self.vals = []
        def bfs(root):
            if not root: return
            level_count = 0 # How many nodes are on the current tree level
            next_level = 1 # How many nodes will be on the next tree level
            self.queue.append(root)
            while self.queue:
                v = self.queue.popleft()
                # We add rightmost node in level first, will be popped when level
                # count is 0 as we moved to the next level
                if level_count == 0: 
                    self.vals.append(v.val)
                    level_count = next_level
                    next_level = 0
                level_count -= 1
                if v.right: 
                    self.queue.append(v.right)
                    next_level += 1
                if v.left: 
                    self.queue.append(v.left)
                    next_level += 1
        bfs(root)
        return self.vals
