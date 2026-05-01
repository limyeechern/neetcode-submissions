class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for t in tasks:
            counts[t] = counts.get(t, 0) + 1
        
        maxHeap = [-v for k,v in counts.items()]

        heapq.heapify(maxHeap)

        cycles = 0
        queue = deque() # (val, timer)

        while maxHeap or queue:
            cycles += 1
            if queue and queue[0][1] == cycles:
                val = queue.popleft()[0]
                heapq.heappush(maxHeap, val)
            if not maxHeap:
                continue
            currentMax = heapq.heappop(maxHeap) + 1
            if currentMax != 0:
                queue.append((currentMax, cycles + n + 1))

        return cycles

            
            