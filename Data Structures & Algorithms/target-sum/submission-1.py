class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} # (index, total)

        def search(index, total):
            if total == target and index == len(nums):
                return 1
            if index >= len(nums):
                return 0
            if (index, total) in cache:
                return cache[(index, total)]
            
            curr = nums[index]
            subtract = search(index + 1, total - curr)
            add = search(index + 1, total + curr)

            cache[(index, total)] = add + subtract
            return add + subtract

        return search(0,0)