# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        dummy = ListNode()
        current = dummy

        # repeat compare
        while True:
            # find the minium number to add to the list
            min_value = 1001
            null_node = 0
            min_index = 0

            # loop through the lists
            for i in range(n):
                if not lists[i]:
                    null_node += 1
                    continue

                value = lists[i].val

                if min_value > value:
                    min_value = value
                    min_index = i
            # all list are empty
            if null_node == n:
                return dummy.next
                
            print(min_index)
            print(lists[min_index].val)
            print("")

            current.next = lists[min_index]
            lists[min_index] = lists[min_index].next
            current = current.next
