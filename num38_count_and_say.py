class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            older_rle = self.countAndSay(n-1)
            newer_rle = ""
            current_ctr = None
            for i, char in enumerate(older_rle):
                if i == 0:
                    current_ctr = (char, 1)
                    continue
                if char == older_rle[i-1]:
                    current_ctr = (char, current_ctr[1]+1)
                else:
                    newer_rle = newer_rle + str(current_ctr[1]) + current_ctr[0]
                    current_ctr = (char, 1)
            newer_rle = newer_rle + str(current_ctr[1]) + current_ctr[0]
            return newer_rle