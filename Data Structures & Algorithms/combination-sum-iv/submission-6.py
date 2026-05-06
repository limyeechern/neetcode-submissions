class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not target:
            return 1
        # ans = [0, 1, 2, 3, 0, ]

        ans = [0] * (target + 1)

        for t in range(target + 1):
            for n in nums:
                if t - n == 0:
                    ans[t] += 1
                elif t - n > 0:
                    ans[t] += ans[t-n]

        print(ans)
        return ans[target]

