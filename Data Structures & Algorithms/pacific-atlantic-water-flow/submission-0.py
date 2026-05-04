class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i,j,ocean,lastHeight):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in ocean or heights[i][j] < lastHeight:
                return
            
            ocean.add((i,j))
            height = heights[i][j]
            for di, dj in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                ni,nj = di + i, dj + j
                dfs(ni, nj, ocean, height)


        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])

        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows-1, j, atlantic, heights[rows-1][j])

        res = []
        for i, j in pacific:
            if (i,j) in atlantic:
                res.append([i,j])
        return res
            