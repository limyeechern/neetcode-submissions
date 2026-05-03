class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i,j):
            if (i,j) in visited:
                return False
            
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False

            if grid[i][j] == "0":
                return False
            
            visited.add((i,j))
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            return True

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j):
                    count += 1
        
        return count
        
            

        