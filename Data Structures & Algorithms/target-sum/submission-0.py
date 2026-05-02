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
            add = search(index + 1, total + curr)
            subtract = search(index + 1, total - curr)
            cache[(index, total)] = add + subtract
            
            return cache[(index, total)]

        print(cache)
        return search(0, 0)
