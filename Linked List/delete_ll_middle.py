# Solved on 16/06/2024
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        mid = n//2
        temp = head
        for i in range(mid-1): temp = temp.next
        temp.next = temp.next.next
        return head
