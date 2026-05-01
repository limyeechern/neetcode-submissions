class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        maxHeap = [(-v,k) for k,v in count.items()]
        heapq.heapify(maxHeap)

        ans = ""
        queue = deque()
        while maxHeap or queue:
            if not maxHeap:
                return ""
            count, char = heapq.heappop(maxHeap)
            if queue:
                val = queue.popleft()
                heapq.heappush(maxHeap, (val[0], val[1]))
            ans += char
            count += 1
            if count != 0:
                queue.append((count, char))

            

        return ans
            

            
            