class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} # (index, total)

        def dfs(index, total):
            if total == target and index == len(nums):
                return 1
            if index >= len(nums):
                return 0
            if (index, total) in cache:
                return cache[(index, total)]

            add = dfs(index + 1, total + nums[index])
            subtract = dfs(index + 1, total - nums[index])

            cache[(index)] = add + subtract
            return add + subtract

        return dfs(0,0)

