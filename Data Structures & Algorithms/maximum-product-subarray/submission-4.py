class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1, 1
        res = nums[0]

        for n in nums:
            tmp = currMax
            currMax = max(currMin * n, currMax * n, n)
            currMin = min(currMin * n, tmp *n , n)
            res = max(res, currMax)
        return res