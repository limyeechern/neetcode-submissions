class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            if grid[i][j] == 0:
                return 0
            if (i,j) in visited:
                return 0
            
            visited.add((i,j))

            top = dfs(i-1, j)
            bottom = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            
            return 1 + top + bottom + left + right

        
        for i in range(rows):
            for j in range(cols):
                maxArea = max(maxArea, dfs(i,j))

        return maxArea