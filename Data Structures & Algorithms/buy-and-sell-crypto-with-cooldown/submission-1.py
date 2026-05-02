class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def search(i, holding):
            if i >= len(prices):
                return 0 
            if (i, holding) in cache:
                return cache[(i, holding)]
            
            if holding:
                sell = search(i + 2, False) + prices[i]
                cooldown = search(i + 1, True)
                cache[(i, holding)] = max(sell, cooldown)
            else:
                buy = search(i + 1, True) - prices[i]
                cooldown = search(i + 1, False)
                cache[(i, holding)] = max(buy, cooldown)
            
            return cache[(i, holding)]

        return search(0, False)
