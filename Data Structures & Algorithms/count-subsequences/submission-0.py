class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        """
            s1, s2, s3 ... sn
        t1
        t2
        t3
        ...
        tm
        """
        rows = len(t)
        cols = len(s)

        grid = [[0 for j in range(len(s) + 1)] for i in range(len(t) + 1)]

        for j in range(cols + 1):
            grid[rows][j] = 1

        for i in range(rows -1, -1, -1):
            for j in range(cols - 1, -1, -1):
                grid[i][j] = grid[i][j + 1]
                if s[j] == t[i]:
                    grid[i][j] += grid[i + 1][j + 1]

        return grid[0][0]

        