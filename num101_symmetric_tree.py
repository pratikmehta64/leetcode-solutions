from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        tree = {}
        curr_depth = 0
        is_symmetric = True
        if root:
            tree[curr_depth] = [root]
        while tree:
            if curr_depth not in tree:
                break
            nodes = tree[curr_depth]
            values = [node.val if node else None for node in nodes]
            if values != values[::-1]:
                return False
            for node in nodes:
                if curr_depth+1 in tree:
                    if node:
                        tree[curr_depth+1].extend([node.left, node.right])
                else:
                    if node:
                        tree[curr_depth+1] = [node.left, node.right]
            curr_depth += 1
        return True
                
            
            
            

        