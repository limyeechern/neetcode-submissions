class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, len(nums) - 1
        hashmap = {}
        for v in nums:
            hashmap[v] = hashmap.get(v,0) + 1
        
        hashset = set()
        for key, v in hashmap.items():
            if v > 1:
                hashset.add(key)

        while l < r:
            if nums[l] == nums[r] and abs(l - r) <= k:
                return True
            if nums[l] not in hashset:
                l += 1
            elif nums[r] not in hashset:
                r -= 1
            else:
                l += 1
        return False

            