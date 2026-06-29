"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}

        pass_1 = head
        while pass_1:
            old_to_new[pass_1] = Node(x=pass_1.val, next=None, random=None)
            pass_1 = pass_1.next

        pass_2 = head
        while pass_2:
            old_to_new[pass_2].next = old_to_new[pass_2.next]
            pass_2 = pass_2.next

        pass_3 = head
        while pass_3:
            old_to_new[pass_3].random = old_to_new[pass_3.random]
            pass_3 = pass_3.next

        return old_to_new[head]