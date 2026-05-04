class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArray = [[] for i in range(len(nums) + 1)]
        freqMap = {}

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1

        for key,v in freqMap.items():
            freqArray[v].append(key)

        res = []
        for i in range(len(freqArray) -1, -1, -1):
            for j in freqArray[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return []

                
                

