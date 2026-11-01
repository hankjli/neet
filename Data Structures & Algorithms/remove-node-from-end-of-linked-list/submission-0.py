# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        length = 0

        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        
        to_rm = length - n

        if to_rm == 0:
            head = head.next
            return head

        i = 0
        cur = head
        while i < to_rm - 1:
            cur = cur.next
            i += 1

        cur.next = cur.next.next
        return head