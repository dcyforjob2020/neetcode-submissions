# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find second half head
        previous = None
        slow, fast = head, head

        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        # reverse second head

        if fast:
            second_half_head = slow.next
            slow.next = None
        else:
            second_half_head = slow
            previous.next = None

        previous = None
        current = second_half_head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        # merge
        reversed_second_half_head = previous
        current = head

        while reversed_second_half_head:
            current_next = current.next
            reversed_second_half_head_next = reversed_second_half_head.next
            current.next = reversed_second_half_head
            reversed_second_half_head.next = current_next
            current = current_next
            reversed_second_half_head = reversed_second_half_head_next

