from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_l3 = ListNode(val=0, next=None)
        l3_ptr = head_l3
        carry = 0
        while l1 or l2:
            if l1 and l2:
                summ = l1.val + l2.val + carry
            elif l1:
                summ = l1.val + carry
            elif l2:
                summ = l2.val + carry
            l3_ptr.next = ListNode(val=summ%10, next=None)
            l3_ptr = l3_ptr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            carry = round(int(summ/10), 1)
        if carry > 0:
            l3_ptr.next = ListNode(val=carry, next=None)
        if head_l3.next:
            return head_l3.next
        return head_l3