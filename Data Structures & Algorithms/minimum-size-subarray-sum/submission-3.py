class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        length = len(nums) + 1
        summation = 0

        while r < len(nums):
            summation += nums[r]
            print(summation)
            while summation >= target:
                length = min(length, r - l + 1)
                summation -= nums[l]
                l += 1
            r += 1
            
        
        return length if length != (len(nums) + 1) else 0
