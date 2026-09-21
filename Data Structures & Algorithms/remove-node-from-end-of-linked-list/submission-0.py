# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        end = count - n
        if end == 0:
            return head.next
        count = 0
        curr = head
        while count < end -1:
            curr = curr.next
            count += 1
        curr.next = curr.next.next
        return head