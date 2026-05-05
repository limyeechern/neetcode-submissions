class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        
        print(diff)
        if sum(diff) < 0:
            return -1
        curr = 0
        ans = 0
        for j in range(len(diff)):
            curr += diff[j]
            if curr < 0:
                curr = 0
                ans = j + 1
            
        return ans
