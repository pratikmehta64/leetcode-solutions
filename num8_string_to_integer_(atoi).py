class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        neg = False
        if not isinstance(s[0], int) and s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        i = 0
        for i in range(len(s)):
            if s[i].isnumeric():
                continue
            else:
                i -= 1
                break
        if i >= 0 and s!='':
            s = int(s[:i+1])
        else:
            return 0
        if neg:
            s = -s
        limit = 2**31
        if s < -limit:
            s = -limit
        elif s > limit-1:
            s = limit-1
        return s