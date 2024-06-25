# Solved on 19/06/2024
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head: return 0
        nums = []
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next
        ret = 0
        for i in range(len(nums)//2):
            ret = max(ret, nums[i] + nums[-(i+1)])
        return ret
