class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # search from the edges, and update all connected Os, the remaining
        # unupdated Os are surrounded and can be flipped
        rows = len(board)
        cols = len(board[0])

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if board[i][j] == "X":
                return
            if board[i][j] == "T":
                return
            
            board[i][j] = "T"
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i + di, j + dj
                dfs(ni, nj)

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
