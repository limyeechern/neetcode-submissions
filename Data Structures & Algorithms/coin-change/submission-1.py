class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        ans = [amount + 1] * (amount + 1)
        # [0,1,2,3,4,1,0,0,0,0,0,0,0]

        for a in range(1, amount + 1):
            for c in coins:
                if a - c == 0:
                    ans[a] = 1
                    break
                elif a - c > 0:
                    ans[a] = min(1 + ans[a - c], ans[a])
        print(ans)
        return ans[amount] if ans[amount] != amount + 1 else -1