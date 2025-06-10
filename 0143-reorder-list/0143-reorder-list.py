# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse second half
        second = slow.next
        slow.next = None
        middle = None
        while (second):
            curr = second.next
            second.next = middle
            middle = second
            second = curr
        
        #Merge
        left = head
        right = middle
        while right:
            temp = left.next
            left.next = right
            temp2 = right.next
            right.next = temp
            left = temp
            right = temp2




        

        