class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, 3, 4, 3, 5, 6, 7]

        if len(nums) == 1:
            return nums[0]
            
        def helper(arr):
            rob1, rob2 = 0, 0

            for n in arr:
                tmp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = tmp
            
            return rob2
        n = len(nums)
        return max(helper(nums[:n-1]), helper(nums[1:]))