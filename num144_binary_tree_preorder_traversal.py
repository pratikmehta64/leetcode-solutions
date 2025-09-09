from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        visited, queue = [], [root]

        while queue:
            node = queue.pop()
            visited.append(node.val)

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return visited