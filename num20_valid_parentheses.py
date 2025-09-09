class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        conjugates = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif char in [")", "}", "]"]:
                if not stack or stack[-1] != conjugates[char]:
                    return False
                stack.pop(-1)
        if stack:
            return False
        return True