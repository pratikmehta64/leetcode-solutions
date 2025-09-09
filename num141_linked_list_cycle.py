from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = []
        ptr = head
        ctr = 0
        while True:
            if not ptr or not ptr.next:
                return False
            if ptr not in nodes:
                nodes.append(ptr)
                ptr = ptr.next
                ctr += 1
            else:
                return True
        return True