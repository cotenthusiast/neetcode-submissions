# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        min_heap = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node is None:
                if not node.left is None:
                    q.append(node.left)
                if not node is None:
                    q.append(node.right)
                heapq.heappush(min_heap, node.val)
        for i in range(k):
            kSmallest = heapq.heappop(min_heap)
        return kSmallest