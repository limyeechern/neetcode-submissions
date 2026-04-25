class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        length = len(nums) + 1
        count = 0

        while r < len(nums):
            count += nums[r]
            while count >= target:
                length = min(r - l + 1, length)
                count -= nums[l]
                l += 1
            r += 1
        if length == len(nums) + 1:
            return 0
        return length
