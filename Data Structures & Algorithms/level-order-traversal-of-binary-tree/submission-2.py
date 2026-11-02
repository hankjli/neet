# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        n_queue = deque()
        n_queue.append(root)

        while len(n_queue) > 0:

            num_pops = len(n_queue)
            level_vals = []
            for i in range(num_pops):
                node = n_queue.popleft()

                if node is not None:
                    level_vals.append(node.val)
                    n_queue.extend([node.left, node.right])
            
            if len(level_vals) > 0:
                res.append(level_vals)

        return res

        
        
        
        