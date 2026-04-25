class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        def helper(start, end):
            midpoint = (start + end) // 2
            if start >= end:
                return -1
            if nums[midpoint] == target:
                return midpoint
            if target < nums[midpoint]:
                return helper(start, midpoint)
            else:
                return helper(midpoint + 1, end)

        return helper(0, len(nums))

        