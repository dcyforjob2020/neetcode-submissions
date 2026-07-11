# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # initialize slow fast node
        s, f = head, head

        # while f and f.next
        while f and f.next:
            # s move 1 node
            # f move 2 nodes
            s = s.next
            f = f.next.next

            # if s equals to f, return True
            if s == f:
                return True

        # no cycle
        return False