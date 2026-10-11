# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root or root is None:
            return []
        q = deque()
        q.append(root)
        return_list = []
        while q:
            current_list = []
            current_q = deque()
            for i in range(len(q)):
                current_q.append(q.popleft())
            while current_q:
                node = current_q.popleft()
                if node is not None:
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
                    current_list.append(node.val)
            return_list.append(current_list)
            current_q.clear()
        return return_list


