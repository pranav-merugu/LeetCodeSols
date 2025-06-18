"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        nodes = {None:None}

        while cur:
            nodes[cur] = Node(cur.val)#create copies of each node
            cur = cur.next
        
        cur = head
        while cur:
            copy = nodes[cur]
            copy.next = nodes[cur.next]
            copy.random = nodes[cur.random]
            cur = cur.next
        
        return nodes[head]



        