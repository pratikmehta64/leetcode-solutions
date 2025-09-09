from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        ptr1 = head
        while ptr1 is not None:
            values.append(ptr1.val)
            ptr1 = ptr1.next
            
        start = 0
        end = len(values)-1
        while start <= end:
            if values[start] != values[end]:
                return False
            start += 1
            end -= 1
        return True
                
        