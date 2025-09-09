class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = {}
        nums_list = []
        for num in nums1:
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
        for num in nums2:
            if num in nums:
                if nums[num] > 0:
                    nums[num] -= 1
                    nums_list.append(num)
        return nums_list
                    