from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ptr = head
        while ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head
        