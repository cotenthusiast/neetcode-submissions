# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # -- Splitting the Linked List --------------------
        slow = 0
        start = head
        while head:
            slow += 1
            head = head.next
            if head!=None:
                head = head.next
        head = start
        for i in range(slow-1):
            head = head.next
        second = head.next
        head.next = None
        first = start

        # -- Reversing the second Linked List -------------
        prev = None
        current = second

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        second = prev

        # -- Intertwining the Linked Lists ----------------
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        