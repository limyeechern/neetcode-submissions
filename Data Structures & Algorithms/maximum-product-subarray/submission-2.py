class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minimum, maximum = 1, 1
        res = nums[0]

        for n in nums:
            tmp = n * maximum
            maximum = max(n * maximum, n * minimum, n)
            minimum = min(tmp, n * minimum, n)
            res = max(maximum, res)

        return res
