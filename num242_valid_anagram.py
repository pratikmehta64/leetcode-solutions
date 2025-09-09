class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {
            c: 0 for c in s
        }
        for c in s:
            count[c] += 1   
        for c in t:
            if c in count:
                count[c] -= 1
            else:
                return False
        for c in count:
            if count[c] != 0:
                return False
        return True