# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #None
        temp = head #3
        leftNode = dummy
        for i in range(left - 1):
            temp = temp.next 
            leftNode = leftNode.next
        prev = None
        i = 0
        while temp and i < (right - left + 1): #2
            nextNode = temp.next #None
            temp.next = prev 
            prev = temp #5
            temp = nextNode #None
            i += 1
        leftNode.next.next = temp
        leftNode.next = prev

        return dummy.next
        