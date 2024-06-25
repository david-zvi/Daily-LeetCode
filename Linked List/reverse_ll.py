# Solved on 18/06/2024
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        old_next = None
        new_next = head
        new_head = head.next
        while True:
            new_next.next = old_next
            if not new_head: break
            old_next, new_next, new_head = new_next, new_head, new_head.next
        return new_next
