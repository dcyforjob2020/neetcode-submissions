# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head

        reverse_head = None
        n = 0

        while cur:
            n += 1
            new_node = ListNode(cur.val, reverse_head)
            reverse_head = new_node

            cur = cur.next

        print(reverse_head.val)
        print(head.val)

        reoder_head = ListNode(-1, head)
        cur = head
        inoder_cur = head.next
        reverse_cur = reverse_head

        for i in range(1, n):
            if i % 2:
                next = reverse_cur.next
                cur.next = reverse_cur
                reverse_cur = next
            else:
                next = inoder_cur.next
                cur.next = inoder_cur
                inoder_cur = next

            cur = cur.next

        cur.next = None

