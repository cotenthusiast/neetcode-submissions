# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        start = head
        tmp = start

        while tmp:
            count += 1
            tmp=tmp.next

        offset_used = False
        
        while count-n > 0:
            count -= 1
            if offset_used:
                head = head.next
            offset_used = True

        if not offset_used:
            return head.next
        
        head.next = head.next.next

        return start
        