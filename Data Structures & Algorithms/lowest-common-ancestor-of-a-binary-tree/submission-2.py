# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node):
            nonlocal res

            if not node:
                return [False, False]

            if res:
                return [False, False]

            left = dfs(node.left)
            right = dfs(node.right)

            if node == q or node == p:
                if (left[0] or left[1]) or (right[0] or right[1]):
                    res = node

                return [True, True]

            if (left[0] or left[1]) and (right[0] or right[1]):
                res = node

            return [left[0] or left[1], right[0] or right[1]]

        dfs(root)

        return res
