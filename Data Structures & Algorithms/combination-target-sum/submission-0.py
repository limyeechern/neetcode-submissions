class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        curr = []

        def dfs(i, total):
            if i >= len(nums):
                return
            if total > target:
                return
            elif total == target:
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i, total + nums[i])
            curr.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        print(ans)
        return ans
            