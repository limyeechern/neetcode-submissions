class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k
        curr = r

        def isACloser(a, b):
            if abs(a - x) < abs(b - x):
                return True
            elif abs(a - x) == abs(b - x):
                return a < b
            return False
            

        while curr < len(arr):
            if isACloser(arr[curr], arr[l]):
                l += 1
                r += 1
            curr += 1

        return arr[l:r]

