# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(-1, l1)

        resident = 0
        cur = dum

        while l1 or l2 or resident:
            if not l1:
                l1 = ListNode()

            if not l2:
                l2 = ListNode()

            total = l1.val + l2.val + resident

            cur.next = ListNode(total % 10)

            resident = total // 10

            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        return dum.next

            