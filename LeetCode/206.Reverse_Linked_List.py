# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
    
        return prev
#https://leetcode.com/problems/reverse-linked-list/
