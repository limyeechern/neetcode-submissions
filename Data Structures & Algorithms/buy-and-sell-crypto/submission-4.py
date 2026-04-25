class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,1,7,1]
        l, r = 0, 0
        profit = 0

        while l < len(prices) and r < len(prices):
            diff = prices[r] - prices[l]
            if diff > 0:
                profit = max(profit, diff)
            else:
                l = r
            r += 1
        return profit

            
            
        