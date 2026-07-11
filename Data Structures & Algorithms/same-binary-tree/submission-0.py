# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time complexity: O(n)
    # space complexity: O(h)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        # if p and q are None
        # return True
        if not p and not q:
            return True
        # if not p
        # return False
        if not p:
            return False
        # if not q
        # return False
        if not q:
            return False

        # recursive case
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)