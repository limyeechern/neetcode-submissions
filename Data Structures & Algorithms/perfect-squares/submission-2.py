class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        squares = []
        for i in range(1, n):
            if i ** 2 <= n:
                squares.append(i ** 2)
        
        ans = [n + 1] * (n + 1)
        
        print(squares)

        for i in range(len(ans)):
            for s in squares:
                if i - s == 0:
                    ans[i] = 1
                    continue
                if i - s > 0:
                    ans[i] = min(ans[i], ans[i - s] + 1)
        
        return ans[n]


        