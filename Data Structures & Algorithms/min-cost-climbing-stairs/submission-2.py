class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        ans = [0] * n 

        for i in range(n - 1, -1, -1):
            if i == n - 1 or i == n -2:
                ans[i] = cost[i]
                continue
            ans[i] = cost[i] + min(ans[i+1], ans[i+2])

        print(ans)
        return min(ans[0], ans[1])
            