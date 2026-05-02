class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1
        
        ans = [0 for i in range(amount + 1)]

        for c in coins:
            for a in range(amount + 1):
                if a - c == 0:
                    ans[a] += 1
                if a - c > 0:
                    ans[a] += ans[a - c] 
        
        return ans[amount]