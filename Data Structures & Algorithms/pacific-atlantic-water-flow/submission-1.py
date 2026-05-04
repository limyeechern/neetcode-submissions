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

            currHeight = heights[i][j]
            for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                ni, nj = i + di, j + dj
                dfs(ni,nj,ocean,currHeight)
    
        for i in range(rows):
            dfs(i,0,pacific,0)
            dfs(i,cols-1,atlantic,0)
            
    
        for j in range(cols):
            dfs(0,j,pacific,0)
            dfs(rows-1,j,atlantic,0)

        res = []
        for (i,j) in pacific:
            if (i,j) in atlantic:
                res.append((i,j))
        
        return res
            