# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time complexity: O(n)
    # space complexity: O(H)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # function 
        # parameter: node
        # return: depth, max diameter
        def depth(node):
            if not node:
                return 0 ,0
            
            left_depth, left_max = depth(node.left)
            right_depth, right_max = depth(node.right)

            return max(left_depth, right_depth) + 1, max(left_depth + right_depth, left_max, right_max)

        return depth(root)[1]
