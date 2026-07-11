# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        # root is None return 0
        if not root:
            return 0

        # recursive case
        # return max of left or right + 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1