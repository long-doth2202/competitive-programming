from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head

        while n > 0:
            p2 = p2.next
            n -= 1
        
        if p2 == None:
            return head.next
        
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next

        return head