from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        quadruplets = []
        for a in range(n-3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a+1, n-2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                left, right = b + 1, n - 1
                while left < right:
                    total = nums[a] + nums[b] + nums[left] + nums[right]
                    if  total == target:
                        quadruplets.append([nums[a], nums[b], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[a] + nums[b] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[a] + nums[b] + nums[left] + nums[right] > target:
                        right -= 1
        return quadruplets