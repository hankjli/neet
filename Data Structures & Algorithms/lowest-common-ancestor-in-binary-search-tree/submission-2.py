# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # the common ancestor x must satisfy p.val <= x <= q.val

        lower = min(p.val, q.val)
        upper = max(p.val, q.val)

        while root is not None:
            if lower <= root.val <= upper:
                return root
            elif root.val < lower:
                root = root.right
            else:
                root = root.left

