from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
## My solution (commented out) ##
#         node_map = {}
#         queue = []
#         level = 0
#         if root:
#             node_map[level] = [root]
#             queue.append((level, root))
#         while queue:
#             level, node = queue.pop(0)
#             if node.left: # Check if the node has children
#                 queue.extend([(level+1, node.left), (level+1, node.right)])
#                 if level+1 not in node_map:
#                     node_map[level+1] = [node.left, node.right]
#                 else:
#                     node_map[level+1].extend([node.left, node.right])
        
#         for level in node_map:
#             for idx, node in enumerate(node_map[level]):
#                 if idx < len(node_map[level])-1:
#                     node.next = node_map[level][idx+1]
#         return root

## Best solution (below) ##
        if not root: return None
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    q.extend([cur.right, cur.left])
        return root
                
                
                
                