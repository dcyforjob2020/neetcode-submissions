# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        fast = head

        while fast and fast.next:
            cur = cur.next
            fast = fast.next.next
            
            if cur == fast:
                return True


        return False