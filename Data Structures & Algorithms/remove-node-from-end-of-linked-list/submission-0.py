# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        curr = ListNode(0, head)
        tmp = curr
        for i in range(length - n):
            curr = curr.next
        tmp1 = curr.next.next
        curr.next = tmp1

        return tmp.next
        
        