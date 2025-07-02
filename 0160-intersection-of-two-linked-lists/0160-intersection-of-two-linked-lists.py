# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        tempB = headB
        countA = 0
        countB = 0
        while tempA:
            tempA = tempA.next
            countA += 1
        while tempB:
            tempB = tempB.next
            countB += 1
        tempA = headA
        tempB = headB
        if countA > countB:
            while (countA - countB > 0):
                tempA = tempA.next
                countA -= 1
        elif countB > countA:
            while (countB - countA > 0):
                tempB = tempB.next
                countB -= 1
        while countA and countB:
            if tempA == tempB:
                return tempA
            else:
                tempA = tempA.next
                tempB = tempB.next
        return None

