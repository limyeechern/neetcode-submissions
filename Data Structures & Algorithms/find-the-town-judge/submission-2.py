class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        deltas = {i:0 for i in range(1, n + 1)}

        for person, t in trust:
            deltas[person] -= 1
            deltas[t] += 1

        for k, v in deltas.items():
            if v == n - 1:
                return k
        return -1

        

