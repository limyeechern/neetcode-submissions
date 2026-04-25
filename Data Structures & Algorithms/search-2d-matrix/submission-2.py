class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols - 1

        while start <= end:
            midpoint = (start + end) // 2
            val = matrix[midpoint // cols][midpoint % cols]

            if val == target:
                return True
            if val < target:
                start = midpoint + 1
            else:
                end = midpoint - 1
        return False
