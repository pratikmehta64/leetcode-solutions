from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for idx in range(len(prices)):
            if prices[idx] < min_price:
                min_price = prices[idx]
            elif prices[idx] - min_price > max_profit:
                max_profit = prices[idx] - min_price
        return max_profit  