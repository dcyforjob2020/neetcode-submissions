# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # # time complexity: O(n + m)
    # # space complexity: O(n + m)
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     # base case
    #     # if list2 is empty, return list1
    #     if not list2:
    #         return list1
    #     # if list1 is empty, return list2
    #     if not list1:
    #         return list2

    #     # recursive case
    #     # if list1 head is smaller than list2
    #     # list1 head next set to list2
    #     # do the method again
    #     # return list1
    #     if list1.val < list2.val:
    #         list1.next = self.mergeTwoLists(list1.next, list2)
    #         return list1
    #     else:
    #         list2.next = self.mergeTwoLists(list1, list2.next)
    #         return list2

    # time complexity: O(n + m)
    # space complexity: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new head node
        prev_head = current = ListNode()

        # while list1 and list2
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 or list2

        return prev_head.next
