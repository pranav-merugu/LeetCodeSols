# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node, res): #depth first search to find max depth
            if not node: 
                return 0 #if node is null, return 0 for depth
            
            left = diameter(node.left, res) #calculate depth, for left and right
            right = diameter(node.right, res)

            res[0] = max(res[0], left + right) #update max

            return max(left, right) + 1 #update with longest depth

        res = [0] #global variable
        
        diameter(root, res)

        return res[0]