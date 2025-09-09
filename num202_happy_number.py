class Solution:
    def isHappy(self, n: int) -> bool:
        n_hist = []
        while len(set(n_hist)) == len(n_hist):
            queue = []
            for digit_str in str(n):
                digit_int = int(digit_str)
                digit_sq = digit_int * digit_int
                queue.append(digit_sq)
            sum_of_squares = sum(queue)
            if sum_of_squares == 1:
                return True
            n_hist.append(sum_of_squares)
            n = sum_of_squares
        return False
        