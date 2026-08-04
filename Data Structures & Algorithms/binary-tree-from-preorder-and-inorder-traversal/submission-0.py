# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}

        for i, val in enumerate(inorder):
            index_map[val] = i

        root = TreeNode(preorder[0])

        for i in range(1, len(preorder)):
            val = preorder[i]
            index = index_map[val]

            parent = None
            is_left = True
            cur = root

            while cur:
                parent = cur

                if index_map[cur.val] > index:
                    cur = cur.left
                    is_left = True
                else:
                    cur = cur.right
                    is_left = False

            if is_left:
                parent.left = TreeNode(val)
            else:
                parent.right = TreeNode(val)

        return root
                

            