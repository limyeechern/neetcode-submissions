class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #  C A T
        # C
        # R
        # A
        # B
        # T    T
        rows = len(text1)
        cols = len(text2)

        grid = [[0 for i in range(cols + 1)] for j in range(rows + 1)]

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = grid[i+1][j+1] + 1
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        return grid[0][0]