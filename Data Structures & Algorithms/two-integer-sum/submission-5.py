class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            hashmap[value] = index

        for index in range(len(nums)):
            curr = nums[index]
            if target - curr in hashmap:
                if hashmap[target - curr] == index: 
                    continue
                return sorted([hashmap[target - curr], index])

