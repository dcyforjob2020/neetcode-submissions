# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True

            left, left_bal = dfs(node.left)
            right, right_bal = dfs(node.right)

            return max(left, right) + 1, abs(left - right) <= 1 and left_bal and right_bal

        return dfs(root)[1]