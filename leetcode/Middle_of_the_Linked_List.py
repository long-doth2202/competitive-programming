from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv = head
        cur = head
        if head == None or head.next == None:
            return head
        while (cur and cur.next != None):
            cur = cur.next.next
            prv = prv.next
        return prv