# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        stack2 = []
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        dummy = ListNode(None)
        temp = dummy
        carry = 0
        while stack1 and stack2:
            sum = stack1.pop(0) + stack2.pop(0) + carry
            carry = sum // 10
            temp.next = ListNode(sum % 10, None)
            temp = temp.next
        
        if stack1:
            while stack1:
                sum = stack1.pop(0) + carry
                carry = sum // 10
                temp.next = ListNode(sum % 10, None)
                temp = temp.next
        elif stack2:
            while stack2:
                sum = stack2.pop(0) + carry
                carry = sum // 10
                temp.next = ListNode(sum % 10, None)
                temp = temp.next

        if carry != 0:
            temp.next = ListNode(carry, None)
        
        return dummy.next




        