from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        insertions = 0
        while i < m+n and j < n:
            if nums1[i] >= nums2[j] and i < m:
                nums1.pop(-1)
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                insertions += 1
            elif nums1[i] < nums2[j] and i < m+insertions:
                i += 1
            else:
                nums1.pop(-1)
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                insertions += 1
