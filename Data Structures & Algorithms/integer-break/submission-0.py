class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        
        def dfs(num):
            if num == 1:
                return 1
            res = 0 if num == n else num
            for i in range(1, num):
                if i in dp:
                    left = dp[i]
                else:
                    left = dfs(i)

                if num - i in dp:
                    right = dp[num - i]
                else:
                    right = dfs(num - i)
                res = max(res, left * right)
            dp[num] = res
            return res

        res = dfs(n)
        return res
        
                
