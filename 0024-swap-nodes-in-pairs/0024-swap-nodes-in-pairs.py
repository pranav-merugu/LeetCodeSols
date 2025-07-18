# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            newHead = ListNode(0, head.next)
        else:
            return head
        temp = head #1, 2, 3, 4
        prev = None
        while temp and temp.next:
            if prev:
                prev.next = temp.next
            prev = temp
            newNext = temp.next.next #null
            temp.next.next = temp #2 > 1
            temp.next = newNext # 1> 3
            temp = newNext #3
        return newHead.next
