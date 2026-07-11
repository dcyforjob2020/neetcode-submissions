# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2:
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()

            total = l1.val + l2.val + carry
            decimal = total % 10
            carry = total // 10
            
            current.next = ListNode(decimal)
            current = current.next
            l1 = l1.next
            l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next

