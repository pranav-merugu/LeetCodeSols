# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        toAdd = []

        def traverse(curNode):
            if curNode:
                toAdd.append(curNode)
                traverse(curNode.left)
                traverse(curNode.right)
        
        traverse(root)
        if toAdd:
            toAdd.pop(0)
        temp = root
        if temp:
            temp.left = None
        while toAdd:
            cur = toAdd.pop(0)
            cur.left = None
            cur.right = None
            temp.right = cur
            temp = temp.right

