class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n == 2 else n
        ans = [0] * (n + 1)
        ans[0] = 0
        ans[1] = 1
        ans[2] = 1

        for i in range(n + 1):
            if i <= 2:
                continue
            ans[i] = ans[i -3] + ans[i -2] + ans[i - 1] 

        return ans[n]