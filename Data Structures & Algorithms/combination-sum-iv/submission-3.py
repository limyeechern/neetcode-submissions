class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1
        ans = [0] * (target+1)
        print(ans)

        for t in range(target+1):
            for num in nums:
                if t - num == 0:
                    ans[t] += 1
                if t-num > 0:
                    ans[t] += ans[t-num]

        print(ans)
        return ans[target]