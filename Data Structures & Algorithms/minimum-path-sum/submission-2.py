class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        costs = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        costs[rows-1][cols-1] = grid[rows-1][cols-1]

        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                if row == rows -1 and col == cols -1:
                    continue
                currCost = grid[row][col]
                costs[row][col] = grid[row][col]
                if row == rows - 1 and col < cols - 1: # last row and still have more columns
                    costs[row][col] = currCost + costs[row][col + 1]
                elif col == cols - 1 and row < rows -1: # last column and still have more rows
                    costs[row][col] = currCost + costs[row + 1][col]
                else:
                    costs[row][col] = currCost + min(costs[row][col + 1], costs[row + 1][col])
        
        return costs[0][0]
                
                

