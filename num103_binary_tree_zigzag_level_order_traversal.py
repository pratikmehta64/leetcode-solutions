from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

####### Grok solution #######
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = [root]
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes in the current level
            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse the current level's values if direction is right-to-left
            if not left_to_right:
                current_level.reverse()
            
            # Append the current level's values to the result
            result.append(current_level)
            
            # Toggle direction for the next level
            left_to_right = not left_to_right
        
        return result