# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur_level = deque()

        cur_level.append(root)
        while len(cur_level) > 0:
            num_pops = len(cur_level)

            rightmost_added = False
            for i in range(num_pops):
                cur = cur_level.pop()

                if cur is None:
                    continue
                else: # have a valid node, should be right-most
                    if not rightmost_added:
                        res.append(cur.val)
                        rightmost_added = True

                    cur_level.appendleft(cur.right)
                    cur_level.appendleft(cur.left)
                    # should not immediately break
                    # need all nodes for next level
                    # both children of cur right-most could both be None
        
        return res
                
