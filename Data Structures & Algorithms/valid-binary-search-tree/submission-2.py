# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        minimum = float('-inf')
        maximum = float('inf')
        return self.investigate(root.left, minimum, root.val) and self.investigate(root.right, root.val, maximum)



    def investigate(self, root, minimum, maximum):
        if root is None:
            return True
        if minimum < root.val < maximum:
            return self.investigate(root.left, minimum, root.val) and self.investigate(root.right, root.val, maximum)
        else:
            return False