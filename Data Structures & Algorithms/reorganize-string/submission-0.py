class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        maxHeap = [(-v,k) for k,v in count.items()]
        heapq.heapify(maxHeap)

        print(maxHeap)

        ans = ""
        cycle = 0
        queue = deque()
        while maxHeap or queue:
            cycle += 1
            if not maxHeap:
                return ""
            count, char = heapq.heappop(maxHeap)
            ans += char
            count += 1
            if count != 0:
                queue.append((count, char, cycle + 1))
            if queue and queue[0][2] == cycle:
                val = queue.popleft()
                heapq.heappush(maxHeap, (val[0], val[1]))

        return ans
            

            
            