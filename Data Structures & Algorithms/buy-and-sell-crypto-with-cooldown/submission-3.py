class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} # (index, holding)

        def search(index, holding):
            if index >= len(prices):
                return 0
            if (index, holding) in cache:
                return cache[(index, holding)]
            
            if holding:
                sell = search(index + 2, False) + prices[index]
                cooldown = search(index + 1, True)
                cache[(index, holding)] = max(sell, cooldown)
            else:
                buy = search(index + 1, True) - prices[index]
                cooldown = search(index + 1, False)
                cache[(index, holding)] = max(buy, cooldown)

            return cache[(index, holding)]

        return search(0, False)