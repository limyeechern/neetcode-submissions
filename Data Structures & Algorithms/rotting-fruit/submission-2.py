class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))

        minutes = 0
        while queue and fresh > 0:
            newQueue = deque()
            minutes += 1
            for _ in range(len(queue)):
                (i,j) = queue.popleft()
                for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        newQueue.append((ni,nj))

            queue = newQueue
        
        return minutes if fresh == 0 else -1
        