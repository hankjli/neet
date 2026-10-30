# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        # [1 2, 3, 4, 5]

        # [1, 2, 3] and [5, 4]

        # [1, 5, 2, 4, 3]

        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next

        l2 = head
        count = 0
        while count < int(length / 2) - 1:
            l2 = l2.next
            count += 1
        

        temp = l2
        l2 = l2.next
        temp.next = None

        prev = None
        while l2 is not None:
            n = l2.next
            l2.next = prev
            prev = l2

            if n is None:
                break
            
            l2 = n
        
        l1 = head.next
        cur = head
        while l2 is not None:
            cur.next = l2
            cur = cur.next
            l2 = l2.next

            if l1 is not None:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            

