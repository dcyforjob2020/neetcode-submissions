# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous = None
        current = head

        # while current exist
        while current:
            # keep next
            next = current.next
            # set current.next to previous
            current.next = previous

            # set previous to current
            # set current to next
            previous = current
            current = next


        # return previous
        return previous