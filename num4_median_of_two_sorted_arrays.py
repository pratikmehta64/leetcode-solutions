from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        o = len(nums1) + len(nums2)
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        
        if (o)%2!=0:
            return nums1[int((o)/2)]
        else:
            return ( nums1[int((o-1)/2)] + nums1[int((o+1)/2)] ) / 2