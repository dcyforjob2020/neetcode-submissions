# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # same tree function
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p:
                return False
            if not q:
                return False

            return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)

        # traverse the tree
        def traverse(node):
            # base case
            # if root is None
            if not node:
                return sameTree(node, subRoot)
            # recursive case
            return sameTree(node, subRoot) or traverse(node.left) or traverse(node.right)

        return traverse(root)
