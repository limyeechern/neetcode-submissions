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
        if not head:
            return None

        oldToNew = {}

        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        tmp = head
        while head:
            old = head
            new = oldToNew[head]
            if old.next:
                new.next = oldToNew[old.next]
            if old.random:
                new.random = oldToNew[old.random]
            head = head.next
        
        return oldToNew[tmp]
        