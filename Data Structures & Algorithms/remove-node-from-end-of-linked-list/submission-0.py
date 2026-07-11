# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count how many nodes
        current = head
        total_nodes = 0

        while current:
            total_nodes += 1
            current = current.next

        # remove the node
        remove_index = total_nodes - n
        print(total_nodes)
        print(remove_index)

        prev_head = ListNode(None ,head)
        previous = prev_head
        current = head

        i = 0

        while current:
            if i == remove_index:
                previous.next = current.next

                return prev_head.next

            previous = current
            current = current.next
            i += 1
