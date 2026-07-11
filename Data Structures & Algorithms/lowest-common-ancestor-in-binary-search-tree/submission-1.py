# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_p(node, target_node, path):
            nonlocal p_path

            if not node:
                return

            find_p(node.left, target_node, path + "L")

            if target_node.val == node.val:
                p_path = path
                return

            find_p(node.right, target_node, path + "R")

        def find_q(node, target_node, path):
            nonlocal q_path

            if not node:
                return

            find_q(node.left, target_node, path + "L")

            if target_node.val == node.val:
                q_path = path
                return

            find_q(node.right, target_node, path + "R")

        p_path = ""
        q_path = ""

        find_p(root, p, "")
        find_q(root, q, "")

        ancestor = root
        i = 0

        while True:
            if i >= len(p_path) or i >= len(q_path):
                break

            if p_path[i] != q_path[i]:
                break
            
            if p_path[i] == "L":
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right

            i += 1

        return ancestor