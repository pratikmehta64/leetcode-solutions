# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = n
        low = 0
        while low <= high:
            mid = (high+low) // 2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid):
                high = mid - 1
            elif not isBadVersion(mid):
                low = mid + 1
        return 1