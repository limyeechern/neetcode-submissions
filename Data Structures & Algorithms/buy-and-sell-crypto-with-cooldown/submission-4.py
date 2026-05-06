class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} # (index, holding)

        def dfs(index, holding):
            if index >= len(prices):
                return 0
            
            if (index, holding) in cache:
                return cache[(index, holding)]

            if holding:
                sell = dfs(index + 2, False) + prices[index]
                cooldown = dfs(index + 1, True)
                cache[(index, holding)] = max(sell, cooldown)
            else: # not holding
                buy = dfs(index + 1, True) - prices[index]
                cooldown= dfs(index + 1, False)
                cache[(index, holding)] = max(buy, cooldown)

            return cache[(index, holding)]

        
        return dfs(0, False)
