class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = {jewels}
        return sum(stone in jewels for stone in stones)
                