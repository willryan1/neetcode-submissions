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
        otn = {}
        otn[None] = None
        curr = head
        c_head = None
        while curr is not None:
            tmp = Node(curr.val)
            if curr == head:
                c_head = tmp
            otn[curr] = tmp
            curr = curr.next

        curr = head
        while curr is not None:
            new = otn[curr]
            new.next = otn[curr.next]
            new.random = otn[curr.random]
            curr = curr.next
        
        return c_head



        