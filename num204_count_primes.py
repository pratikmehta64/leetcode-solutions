class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [1 for _ in range(n+1)]
        num = 2
        while num*num < n:
            if nums[num]:
                for i in range(num*num, n, num):
                    nums[i] = 0
            num+=1
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        return sum(nums)-3