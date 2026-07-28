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
        index_node_map = {}

        cur = head
        new_head = Node(-1)
        new_cur = new_head

        while cur:
            new_cur.next = Node(cur.val)
            index_node_map[cur] = new_cur.next

            new_cur = new_cur.next
            cur = cur.next

        cur = head
        
        while cur:
            new_cur = index_node_map[cur]

            if cur.random:
                new_cur.random = index_node_map[cur.random]

            cur = cur.next

        return new_head.next