class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation % 2 != 0:
            return False
        
        target = summation / 2

        hashset = set()
        hashset.add(0)

        for n in nums:
            copy = hashset.copy()
            for i in hashset:
                copy.add(i + n)
                if target in copy:
                    return True
            hashset = copy

        return False
            