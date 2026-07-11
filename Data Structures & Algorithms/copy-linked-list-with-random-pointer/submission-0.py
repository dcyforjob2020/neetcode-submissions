"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        current = head
        new_current = None
        dummy = Node(0)
        previous_new_current = dummy

        while current:
            new_current = Node(current.val)
            previous_new_current.next = new_current
            node_map[current] = new_current
            previous_new_current = previous_new_current.next
            current = current.next

        current = head
        new_current = dummy.next

        while current:
            if current.random:
                new_current.random = node_map[current.random]
                
            current = current.next
            new_current = new_current.next

        return dummy.next