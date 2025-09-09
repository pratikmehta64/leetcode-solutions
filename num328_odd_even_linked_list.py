from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # Handle empty or single-node list
            return head
        
        odd = head  # Points to the current odd node
        even = head.next  # Points to the current even node
        even_head = even  # Save the head of the even list for later connection
        
        while even and even.next:  # Continue until we can't move forward
            odd.next = even.next  # Link odd to the next odd node
            odd = odd.next  # Move odd pointer forward
            even.next = odd.next  # Link even to the next even node
            even = even.next  # Move even pointer forward
        
        odd.next = even_head  # Connect the odd list to the even list
        return head
            