from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ptr_one = dummy
        ptr_two = dummy
        for _ in range(n+1):
            ptr_one = ptr_one.next

        while ptr_one:
            ptr_one = ptr_one.next
            ptr_two = ptr_two.next
        if ptr_two.next:
            ptr_two.next = ptr_two.next.next
        return dummy.next
        
        
                
        
        
            