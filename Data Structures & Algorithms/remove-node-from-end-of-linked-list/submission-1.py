# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre = None
        cur = head

        while cur:
            next = cur.next

            cur.next = pre

            pre = cur
            cur = next

        reverse_head = pre
        pre = None
        cur = reverse_head
        i = 0

        while cur:
            i += 1
            
            if i == n:
                cur = cur.next
                continue

            next = cur.next

            cur.next = pre

            pre = cur
            cur = next

        return pre