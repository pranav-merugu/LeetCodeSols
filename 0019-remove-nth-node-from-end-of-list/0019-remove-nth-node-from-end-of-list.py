# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head #1
        fast = head #1
        for i in range(n): # n = 2
            fast = fast.next # fast = 1 -> 2 -> 3

        if (fast == None): #edge case, when n = sz
            head = head.next
            return head

        prev = None
        while fast: #3 -> 4 -> 5 -> None
            fast = fast.next #fast = 4 -> 5 -> None
            prev = slow #prev = 1 -> 2 -> 3
            slow = slow.next #slow = 2 -> 3 -> 4
    
        prev.next = slow.next
        
        return head

        