# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        diam = self.maxDepth(root.left) + self.maxDepth(root.right)
        l_diam = self.diameterOfBinaryTree(root.left)
        r_diam = self.diameterOfBinaryTree(root.right)

        return max(diam, l_diam, r_diam)
    
    def maxDepth(self, root):
        if root is None:
            return 0
        
        l_depth = 1 + self.maxDepth(root.left)
        r_depth = 1 + self.maxDepth(root.right)

        return max(l_depth, r_depth)