class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = int('-'+str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])
        threshold = 2**31
        if x < -threshold or x > threshold - 1:
            return 0
        return x