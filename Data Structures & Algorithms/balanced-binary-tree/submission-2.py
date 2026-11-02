# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        l_height = self.getHeight(root.left)
        r_height = self.getHeight(root.right)
        
        return 0 <= abs(l_height - r_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    


    def getHeight(self, root):
        if root is None:
            return 0
        
        l_height = 1 + self.getHeight(root.left)
        r_height = 1 + self.getHeight(root.right)

        return max(l_height, r_height)