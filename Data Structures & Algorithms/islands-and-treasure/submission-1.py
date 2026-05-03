class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        inf = 2**31 - 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))

        while queue:
            (i,j) = queue.popleft()
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < rows and nj >= 0 and nj < cols and grid[ni][nj] == inf:
                    grid[ni][nj] = grid[i][j] + 1
                    queue.append((ni,nj))

        