class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hashmap = {}
        for t in tasks:
            hashmap[t] = hashmap.get(t, 0) + 1

        maxHeap = [(-v) for k, v in hashmap.items()]
        heapq.heapify(maxHeap)

        cycles = 0
        queue = deque() # [count, time]
        # 
        # (1, 3), (1, 4)
        while maxHeap or queue:
            cycles += 1
            if queue and queue[0][1] == cycles:
                heapq.heappush(maxHeap, queue.popleft()[0])
            if not maxHeap:
                continue
            val = heapq.heappop(maxHeap) + 1
            if val != 0:
                queue.append((val, cycles + n + 1))

        return cycles
            