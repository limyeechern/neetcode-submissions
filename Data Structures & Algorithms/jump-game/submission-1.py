class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = [False for i in range(len(nums))]
        ans[len(nums) - 1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(0, nums[i] + 1):
                if ans[i + j]:
                    ans[i] = True
                    break
        
        return ans[0]
