class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation % 2 != 0:
            return False

        target = summation / 2
        
        hashset = set()
        hashset.add(0)

        for n in nums:
            newSet = hashset.copy()
            for t in hashset:
                newSet.add(t + n)
                if target in newSet:
                    return True
            hashset = newSet

        return False
        