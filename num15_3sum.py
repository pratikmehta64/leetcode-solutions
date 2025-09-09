from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        if not nums:
            return list(solutions)
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            a = nums[i]
            j = i+1
            k = n-1
            while j < k:
                b, c = nums[j], nums[k]
                summ = a + b + c
                if summ > 0:
                    k -= 1
                elif summ < 0: 
                    j += 1
                else:
                    solutions.add((a,b,c))
                    j += 1
                    k -= 1
        return list(solutions)