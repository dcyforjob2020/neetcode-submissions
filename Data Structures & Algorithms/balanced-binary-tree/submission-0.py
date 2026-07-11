# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # depth function
        def depth(node):
            # base case
            if not node:
                return 0

            # recursive case
            # get left height
            # get right height
            left_height = depth(node.left)
            right_height = depth(node.right)

            # -1 means unbalanced
            # if left or right height is -1 or absolute left height - right height > 1
            # return -1
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            # return max left right height + 1
            return max(left_height, right_height) + 1

        return depth(root) != -1