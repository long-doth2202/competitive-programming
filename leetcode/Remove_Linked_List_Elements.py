# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head

        while (cur != None):
            if cur == head and cur.val == val:
                head = head.next
                cur = cur.next
            elif cur.next and cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head