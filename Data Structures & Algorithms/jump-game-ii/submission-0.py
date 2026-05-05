class Solution:
    def jump(self, nums: List[int]) -> int:
        # [2,4,1,1,1,1]
        #    l.r 
        l, r = 0, 0
        steps = 0

        while r < len(nums) -1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            steps += 1
        return steps

        