class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1

        # [0, 1, 2, 3, 4, 6, 9, 0]

        for num in range(2, n + 1):
            dp[num] = num if num != n else 0
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num - i])
        
        return dp[n]

        