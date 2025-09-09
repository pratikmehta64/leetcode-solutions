from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = {}
        output = []
        is_symmetric = True
        curr_depth=0
        if root:
            tree[curr_depth] = [root]
        while tree:
            if curr_depth not in tree:
                break
            nodes = tree[curr_depth]
            values = [node.val for node in nodes if node]
            if values:
                output.append(values)
            for node in nodes:
                if curr_depth+1 in tree:
                    if node:
                        tree[curr_depth+1].extend([node.left, node.right])
                else:
                    if node:
                        tree[curr_depth+1] = [node.left, node.right]
            curr_depth += 1
        return output