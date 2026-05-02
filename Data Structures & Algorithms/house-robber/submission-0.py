class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = [0] * len(nums)

        # [9,10,3,6]
        
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = tmp

        return max(rob1, rob2)
        