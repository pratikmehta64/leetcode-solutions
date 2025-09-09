class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        count = 0
        while True:
            if nums[idx] == 0:
                del nums[idx]
                count += 1
                idx -= 1
            if idx >= len(nums) -1:
                break
            idx += 1
        nums.extend([0]*count)