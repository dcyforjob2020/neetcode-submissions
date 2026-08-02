# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = deque()

        if root:
            queue.append(root)

        while queue:
            level_nodes = len(queue)

            most_right_node = None

            for _ in range(level_nodes):
                most_right_node = queue.popleft()

                if most_right_node.left:
                    queue.append(most_right_node.left)

                if most_right_node.right:
                    queue.append(most_right_node.right)

            res.append(most_right_node.val)

        return res

