class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        grid = [[0 for i in range(cols)] for j in range(rows)]
        grid[rows-1][cols-1] = 1

        for row in range(rows -1, -1,-1):
            for col in range(cols -1, -1, -1):
                if row + 1 < rows and obstacleGrid[row+1][col] != 1:
                    grid[row][col] += grid[row+1][col]
                if col + 1 < cols and obstacleGrid[row][col+1] != 1:
                    grid[row][col] += grid[row][col+1]
        
        return grid[0][0]
