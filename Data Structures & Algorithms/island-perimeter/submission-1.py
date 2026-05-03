class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        visited = set()

        def dfs(i, j):
            nonlocal perimeter

            if i < 0 or j < 0 or i >= rows or j>= cols: # outside of the grid
                return 1

            if grid[i][j] == 0: # in water
                return 1

            if (i,j) in visited:
                return 0
            visited.add((i,j))

            top = dfs(i-1, j)
            bottom = dfs(i+1,j)
            left = dfs(i,j-1)
            right = dfs(i,j+1)
            total = top + bottom + left + right

            perimeter += total
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return perimeter


            
            