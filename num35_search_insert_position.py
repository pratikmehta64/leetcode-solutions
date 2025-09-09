from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            if target <= nums[0]:
                return 0
            if target > nums[n-1]:
                return n
            elif n == 2:
                return 1
        mini = 0
        mid = int(len(nums) / 2)
        maxi = n-1
        
        while mini <= maxi:
            mid = mini+(maxi - mini)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                mini = mid + 1
            else:
                maxi = mid - 1
        return mini