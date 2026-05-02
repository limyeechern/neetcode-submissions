class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minimum, maximum = 1, 1
        res = nums[0]

        for n in nums:
            tmp = n * maximum
            maximum = max(n*minimum, n*maximum, n)
            minimum = min(n*minimum, tmp, n)
            res = max(maximum, res)
            print(maximum)

        return res
