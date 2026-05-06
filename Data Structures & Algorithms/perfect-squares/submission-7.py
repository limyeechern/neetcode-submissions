class Solution:
    def numSquares(self, n: int) -> int:
        
        squares = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]

        # [0, 1, 2, 3, 1, 0, 0, 0]
        ans = [n + 1] * (n + 1)

        for a in range(n + 1):
            for s in squares:
                if s > a:
                    break
                if a - s == 0:
                    ans[a] = 1
                    break
                if a - s > 0:
                    ans[a] = min(ans[a], 1 + ans[a - s])

        print(ans)
        return ans[n] if ans[n] != (n+1) else 1
        