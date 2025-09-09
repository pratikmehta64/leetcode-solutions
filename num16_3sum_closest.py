class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0]+nums[1]+nums[2]
        n = len(nums)
        for i in range(n-2):
            a = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                if abs(target - (a+b+c)) < abs(target - closest_sum):
                    closest_sum = a+b+c
                
                if a+b+c < target:
                    j += 1
                elif a+b+c > target:
                    k -= 1
                else:
                    return target
                    
        return closest_sum