class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # [1, 1, 2]
        # [1, 2]
        # [2]
        # []
        ans = []


        if len(nums) == 0:
            return [[]]
        
        permutations = self.permuteUnique(nums[1:])
        for p in permutations:
            for i in range(len(p) + 1):
                if i > 0 and p[i - 1] == nums[0]:
                    break
                pcopy = p.copy()
                pcopy.insert(i, nums[0])
                ans.append(pcopy)
    

        return ans
