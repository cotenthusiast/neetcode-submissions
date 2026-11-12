# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = ""
        if root is None:
            return string
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node is None:
                string += "@/"
            else:
                string = string + str(node.val) + "/"
                q.append(node.left)
                q.append(node.right)

        return string

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "@/":
            return None
        nodes = data.split("/")
        root = TreeNode(nodes[0])
        i = 1
        q = deque()
        q.append(root)
        while q and i < len(nodes):
            node = q.popleft()
            left = nodes[i]
            i += 1
            right = nodes[i]
            i += 1
            if left != "@":
                left = TreeNode(int(left))
                node.left = left
                q.append(left)
            if right != "@":
                right = TreeNode(int(right))
                node.right = right
                q.append(right)

        return root