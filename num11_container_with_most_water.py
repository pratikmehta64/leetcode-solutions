from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        i,j = 0, n-1
        while i < j:
            area = (j-i) * min(height[i], height[j])
            if area > max_area:
                max_area = area
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area