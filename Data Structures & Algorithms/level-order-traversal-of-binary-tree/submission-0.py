# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return []

        queue = [(root, 0)]

        for e in queue:
            node = e[0]
            level = e[1]

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

            if len(res) <= level:
                res.append([])

            res[level].append(node.val)

        return res

            

