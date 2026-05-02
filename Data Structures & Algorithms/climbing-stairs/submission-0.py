class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        ans = [0] * n
        ans[n - 1] = 1
        ans[n - 2] = 2
        for i in range(n - 1, -1, -1):
            if i == n-1 or i == n - 2:
                continue
            ans[i] = ans[i + 1] + ans[i + 2]

        return ans[0]