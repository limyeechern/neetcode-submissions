class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = {} # all the people that trusts 'key'
        outgoing = {} # all the people that 'key' trusts

        for i in range(1, n + 1):
            incoming[i] = []
            outgoing[i] = []

        for key, trusts in trust: # 'key' 'trusts' person
            outgoing[key].append(trusts)
            incoming[trusts].append(key)

        print(incoming)
        print(outgoing)

        potentialJudge = []
        for k, v in incoming.items():
            if len(v) == n - 1:
                potentialJudge.append(k)
        
        potentialJudge2 = []
        for j in potentialJudge:
            if len(outgoing[j]) == 0:
                potentialJudge2.append(j)

        return potentialJudge2[0] if len(potentialJudge2) == 1 else -1

