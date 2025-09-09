class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k:
            nums.insert(0,nums[-1])
            del nums[-1]
            k -= 1