import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # [10, 11 ... 26]
        sumWeights = sum(weights)
        start, end = max(weights), sumWeights
        ans = end

        while start <= end:
            midpoint = (start + end) // 2
            expectedDays = 1
            currentWeight = 0
            for w in weights:
                if currentWeight + w > midpoint:
                    expectedDays += 1
                    currentWeight = 0
                currentWeight += w
            if expectedDays <= days:
                ans = min(ans, midpoint)
                end = midpoint - 1
            else:
                start = midpoint + 1
        
        return ans



        