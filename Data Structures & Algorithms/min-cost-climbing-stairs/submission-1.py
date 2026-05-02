class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        ans = [0] * n
        ans[n-1] = cost[n-1]
        ans[n-2] = cost[n-2]

        for i in range(n - 1, -1, -1):
            if i == n-1 or i == n - 2:
                continue
            ans[i] = cost[i] + min(ans[i + 1], ans[i + 2])

        return min(ans[0], ans[1])
        