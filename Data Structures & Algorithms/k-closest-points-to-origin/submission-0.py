import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []

        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            dists.append((-dist, p))

        heapq.heapify(dists)

        while len(dists) > k:
            heapq.heappop(dists)
        
        ans = []
        for j in dists:
            ans.append(j[1])

        return ans