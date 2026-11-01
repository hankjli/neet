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


        real_to_copy = {}
        cur = head

        while cur is not None:
            real_to_copy[cur] = Node(cur.val, cur.next, cur.random)
            cur = cur.next

        i = 0
        new_head = None
        cur = head
        while cur is not None:
            if i == 0: # initialize head
                new_head = real_to_copy[cur]
                if cur.next is not None:
                    new_head.next = real_to_copy[cur.next]
                if cur.random is not None:
                    new_head.random = real_to_copy[cur.random]
                
            else:
                cur_copy = real_to_copy[cur]
                if cur.next is not None:
                    cur_copy.next = real_to_copy[cur_copy.next]
                if cur.random is not None:
                    cur_copy.random = real_to_copy[cur_copy.random]

            i += 1 
            cur = cur.next

        return new_head
