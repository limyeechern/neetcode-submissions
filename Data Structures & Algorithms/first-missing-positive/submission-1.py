class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set(nums)
        
        smallest = float('inf')
        for n in nums:
            key = n + 1
            if key > 0 and key not in hashset:
                smallest = min(key, smallest)
        
        if 1 not in hashset:
            smallest = 1
        return smallest
        