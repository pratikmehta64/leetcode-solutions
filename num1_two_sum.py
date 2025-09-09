from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx_1, num in enumerate(nums):
            hyp = target - num
            if num not in lookup:
                lookup[num] = [idx_1]
            else:
                lookup[num].append(idx_1)
            try:
                indices = lookup[hyp]
                if hyp == num and len(indices) == 1:
                    raise IndexError
            except IndexError:
                continue
            except KeyError:
                continue
            indices = indices[0]
            return [idx_1, indices]