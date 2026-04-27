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
        
        onm = {} # old new map
        curr = head
        while curr:
            onm[curr] = Node(curr.val)
            curr = curr.next

        tmp = head
        while head:
            old = head
            new = onm[old]

            if old.next:
                new.next = onm[old.next]
            
            if old.random:
                new.random = onm[old.random]

            head = head.next

        return onm[tmp]
