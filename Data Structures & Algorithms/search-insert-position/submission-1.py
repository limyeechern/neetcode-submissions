class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:        
        def helper(start, end):
            if start >= end:
                return start
            midpoint = (start + end) // 2
            if target == nums[midpoint]:
                return midpoint
            if target < nums[midpoint]:
                return helper(start, midpoint)
            else:
                return helper(midpoint + 1, end)

        return helper(0, len(nums))
