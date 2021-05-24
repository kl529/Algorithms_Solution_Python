# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #뒤집기
    def reverseList(self, head : ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next,prev
            prev, node = node, next
        return prev
    
    #파이썬 리스트로 바꾸기
    def toList(self, node: List) ->List:
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    #다시 연결리스트 만들기
    def toReversedLinkedList(self, result:str)-> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            #두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            #몫과 나머지 계산
            carry, val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next
    
#https://leetcode.com/problems/add-two-numbers/
