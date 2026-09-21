# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_str = ''
        second_str = ''
        curr = l1
        while curr:
            first_str = str(curr.val) + first_str
            curr = curr.next
        curr = l2
        while curr:
            second_str = str(curr.val) + second_str
            curr = curr.next
        result = int(first_str) + int(second_str)
        res_repr = str(result)
        head = ListNode()
        curr = head
        for i in range(len(res_repr)):
            other = ListNode()
            other.val = int(res_repr[len(res_repr) - i -1])
            curr.next = other
            curr = other
        return head.next


