# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        size = 0
        ret = None
        start = head
        while head != None:
            if count == k-1:
                ret = head
            count += 1
            size += 1
            head = head.next
        
        head = start
        previous_tail = None

        for _ in range(size // k):
            first = head
            prev = None
            for i in range(k):
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            if previous_tail:
                previous_tail.next = prev

            first.next = head
            previous_tail = first

        return ret if ret else head