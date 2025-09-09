class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_chars = {}
        for idx, char in enumerate(s):
            if char not in unique_chars:
                unique_chars[char] = [idx]
            else:
                unique_chars[char].append(idx)
        
        for char in unique_chars:
            if len(unique_chars[char]) == 1:
                return unique_chars[char][0]
        return -1