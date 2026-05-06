class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        # [inf, 1, 2, inf, inf, inf]

        ans = [float('inf')] * (amount + 1)

        for a in range(amount + 1):
            for c in coins:
                if a - c == 0:
                    ans[a] = 1
                    continue
                elif a - c > 0:
                    ans[a] = min(ans[a], ans[a-c] + 1)
        
        print(ans)
        return ans[amount] if ans[amount] != float('inf') else -1