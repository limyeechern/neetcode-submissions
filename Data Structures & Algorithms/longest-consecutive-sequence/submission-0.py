class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxCount = 0
        for i in nums:
            count = 0
            key = i
            while key in numSet:
                count += 1
                key -= 1 
            maxCount = max(count, maxCount)
        return maxCount
