from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx, count = 1, 1
        while(idx < len(nums)-1):
            if nums[idx-1] == nums[idx+1]:
                count += 1
                nums.pop(idx)
            else:
                idx += 1
        return len(nums)