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
            for k in hashset:
                copy.add(n + k)
                if target in hashset:
                    return True
            hashset = copy
        return False