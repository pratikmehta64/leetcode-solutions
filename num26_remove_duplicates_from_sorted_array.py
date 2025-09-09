class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 1
        while idx < len(nums):
            if nums[idx] == nums[idx-1]:
                del nums[idx]
            else:
                idx += 1
            
            
        return len(nums)