class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        nums_dup = []
        if len(nums) == 1:
            return nums[0]
        else:
            for num in nums:
                if num not in nums_dup:
                    nums_dup.append(num)
                else:
                    del nums_dup[nums_dup.index(num)]
        return nums_dup[0]
        """
        a = 0
        for num in nums:
            a ^= num
        return a
            