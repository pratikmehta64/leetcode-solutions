from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        cutoff = int(n/2)
        if n == 3:
            root = TreeNode(val=nums[1])
            root.left = TreeNode(val=nums[0])
            root.right = TreeNode(val=nums[2])
        elif n <= 2:
            root = TreeNode(val=nums[-1])
            if n > 1:
                root.left = TreeNode(val=nums[0])
        elif n > 3:
            root = self.sortedArrayToBST([nums[cutoff]])
            root.left = self.sortedArrayToBST(nums[:cutoff])
            root.right = self.sortedArrayToBST(nums[cutoff+1:])
        return root
            
            