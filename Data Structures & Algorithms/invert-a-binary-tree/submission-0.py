# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        # if root is None, then return the root
        if not root:
            return root

        # recursive case
        # swap root.left and root.right
        root.left, root.right = root.right, root.left
        # recursive the root.left
        # recursive the root.right
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return root
        return root
