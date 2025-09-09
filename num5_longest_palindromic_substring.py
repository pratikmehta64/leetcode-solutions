class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s 
        
        idx_1 = 0
        idx_2 = n-1
        max_test_len = n
        # A function to return substring start and end indices 
        # given a string and max len
        def calc_ss_indices(max_test_len, n):
            num_windows = n - max_test_len + 1
            ss_indices = []
            for i in range(num_windows):
                window_start_idx = i
                window_end_idx = i + max_test_len - 1
                ss_indices.append((window_start_idx, window_end_idx))
            return ss_indices

        while max_test_len > 1:
            # Test substrings of length max_test_len for palindromes
            
            ss_indices = calc_ss_indices(max_test_len, n)
            for (start_idx, end_idx) in ss_indices:
                idx_1, idx_2 = start_idx, end_idx
                is_palindrome = True
                if idx_1 > 0 and s[idx_1:idx_2+1] == s[idx_2:idx_1-1:-1]:
                    is_palindrome = True
                    break
                elif idx_1 == 0 and s[idx_1:idx_2+1] == s[idx_2::-1]:
                    is_palindrome = True
                    break
                else:
                    is_palindrome = False
                
            if is_palindrome:
                return s[start_idx:end_idx+1]
            else:
                max_test_len -= 1
        return s[0]
