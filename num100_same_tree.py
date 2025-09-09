from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = [p]
        q_queue = [q]
        while p_queue or q_queue:
            if p_queue:
                p_node = p_queue.pop(0)
            if q_queue:
                q_node = q_queue.pop(0)
            if p_node and q_node and p_node.val == q_node.val:
                p_queue.extend([p_node.left, p_node.right])
                q_queue.extend([q_node.left, q_node.right])
            elif not p_node and not q_node:
                continue
            else:
                return False
            
        return True

        