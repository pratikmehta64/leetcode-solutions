from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A_nodes = []
        B_nodes = []
        A_ptr = headA
        B_ptr = headB
        intersect = False
        while A_ptr or B_ptr:
            A_nodes.append(A_ptr)
            B_nodes.append(B_ptr)
            if A_ptr in B_nodes:
                return A_ptr
            if B_ptr in A_nodes:
                return B_ptr
            if A_ptr:
                A_ptr = A_ptr.next
            if B_ptr:
                B_ptr = B_ptr.next