class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 == stone2:
                continue
            elif -stone1 < -stone2: # from maxheap, values are negative
                heapq.heappush(stones, stone2 - stone1)
            else:
                heapq.heappush(stones, stone1 - stone2)

        return -stones[0] if stones else 0