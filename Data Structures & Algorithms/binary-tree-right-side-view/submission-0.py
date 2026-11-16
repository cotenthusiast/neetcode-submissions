# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []

        def traverse(root, path):
            if root is None:
                paths.append(path)
                return
            traverse(root.right, path + [root.val])
            traverse(root.left, path + [root.val])
    
        paths = []

        traverse(root, [])
        final_path = []

        for path in paths:
            if len(path) > len(final_path):
                final_path += path[len(final_path)::]

        return final_path