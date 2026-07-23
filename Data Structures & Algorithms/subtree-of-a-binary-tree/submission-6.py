# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = False

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not q:
                return False
            if not p:
                return False
            if p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def dfs(node):
            nonlocal subRoot
            nonlocal result

            if not node:
                return 

            if node.val == subRoot.val:
                result = isSameTree(node, subRoot)

                if result:
                    return

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return result