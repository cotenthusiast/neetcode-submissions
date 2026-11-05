# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def height(root):
            if root is None:
                return 0
            return 1 + max(height(root.right), height(root.left))

        def balanced(root):
            if root is None:
                return True
            return abs(height(root.right) - height(root.left)) <= 1 and balanced(root.left) and balanced(root.right)

        return balanced(root)
        
        