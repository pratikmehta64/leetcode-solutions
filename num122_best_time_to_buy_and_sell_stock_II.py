class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i, j = 0 , 1
        holding = False
        profit = 0
        while j < len(prices):
            if holding == False:
                if prices[i] < prices[j]:
                    holding = True
                    profit -= prices[i]
            if holding == True:
                if prices[i] > prices[j]:
                    holding = False
                    profit += prices[i]
                elif j == len(prices) - 1:
                    holding = False
                    profit += prices[j]
                  
            i += 1
            j += 1    
        return profit