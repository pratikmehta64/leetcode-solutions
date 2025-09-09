class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([str(c) for c in s if c.isalnum()]).lower()
        i = 0
        j = len(s)-1
        if j<1:
            return True
        while i<=j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True