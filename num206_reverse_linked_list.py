from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        node = head
        if not head:
            return None
        while node is not None:
            node_list.append(node)
            node = node.next
        for idx in range(len(node_list))[:0:-1]:
            node_list[idx].next = node_list[idx-1]
            # node_list.pop(idx)
        node_list[0].next = None
        return node_list[-1]