from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idxs_to_pop = []
        for idx, element in enumerate(nums):
            if element == val:
                idxs_to_pop.append(idx)
        for meta_idx, idx in enumerate(idxs_to_pop):
            nums.pop(idx - meta_idx)
        return len(nums)