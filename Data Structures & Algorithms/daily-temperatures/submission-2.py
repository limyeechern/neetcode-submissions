class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]

        n = len(temperatures)
        res = [0 for i in range(n)]

        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1

            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i

        return res
            
            