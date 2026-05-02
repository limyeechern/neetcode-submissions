class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1
            
        ans = [0] * (target + 1)

        nums.sort()

        for t in range(len(ans)):
            for n in nums:
                if t - n == 0:
                    ans[t] += 1
                if t - n > 0:
                    ans[t] += ans[t - n]

        return ans[target]
