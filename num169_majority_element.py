from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Pratik's solution
        counts = {}
        n = len(nums)
        for idx, element in enumerate(nums):
            if element not in counts:
                counts[element] = 1
            else:
                counts[element] += 1
            if counts[element] > n/2:
                return element                
                
                