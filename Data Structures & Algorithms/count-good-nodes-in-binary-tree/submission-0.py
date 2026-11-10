# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def traverse(root, current_max):

            if root is None:
                return 0

            if root.val >= current_max:
                current_max = root.val
                return 1 + traverse(root.right, current_max) + traverse(root.left, current_max)
            else:
                return 0 + traverse(root.right, current_max) + traverse(root.left, current_max)

        return traverse(root, root.val)