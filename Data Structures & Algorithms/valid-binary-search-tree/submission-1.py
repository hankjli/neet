# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # treat each node as root of a subtree

        return self.validateSub(root, None, None)

    
    def validateSub(self, root, lower, upper):
        if root is None:
            return True
        
        if lower is None and upper is None:
            return (
                True 
                and self.validateSub(root.left, None, root.val) 
                and self.validateSub(root.right, root.val, None)
            )
        elif lower is None:
            return (
                root.val < upper
                and self.validateSub(root.left, None, root.val)
                and self.validateSub(root.right, root.val, upper)
            )
        elif upper is None:
            return (
                root.val > lower
                and self.validateSub(root.left, lower, root.val)
                and self.validateSub(root.right, root.val, None)
            )
        else:
            return (
                root.val > lower
                and root.val < upper
                and self.validateSub(root.left, lower, root.val)
                and self.validateSub(root.right, root.val, upper)
            )