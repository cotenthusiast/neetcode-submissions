# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        heap = []

        # Add each non-empty list's first node
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        current = dummy

        while heap:
            value, i, smallest = heapq.heappop(heap)

            # Attach the actual node to the merged list
            current.next = smallest
            current = current.next

            # Add this list's next candidate
            if smallest.next:
                heapq.heappush(
                    heap,
                    (smallest.next.val, i, smallest.next)
                )

        return dummy.next