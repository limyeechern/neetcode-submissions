class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # [1, 2, 3]
        # [2, 3], [3,2]
        # [3]
        # []
        
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        ans = []
        for p in perms:
            for i in range(len(p) + 1):
                pcopy = p.copy()
                pcopy.insert(i, nums[0])
                ans.append(pcopy)
    
        return ans
        


        