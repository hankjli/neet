# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.checkIsGood(root, root.val)
    

    def checkIsGood(self, root, prevMax):
        if root is None:
            return 0

        if root.val >= prevMax:
            return 1 + self.checkIsGood(root.left, root.val) + self.checkIsGood(root.right, root.val)
        else: # root.val < prevMax, not a good node, continue to traverse
            return 0 + self.checkIsGood(root.left, prevMax) + self.checkIsGood(root.right, prevMax)