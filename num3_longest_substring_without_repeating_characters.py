class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Improved upon by Grok
        n = len(s)
        max_len = 0
        char_index = {}
        i = 0
        for j in range(n):
            if s[j] in char_index and char_index[s[j]] >= i:
                i = char_index[s[j]] + 1
            max_len = max(max_len, j-i+1)
            char_index[s[j]] = j
        return max_len