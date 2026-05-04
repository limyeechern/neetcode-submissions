class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}

        for s in strs:
            newS = "".join(sorted(s))
            newList = hashset.get(newS, [])
            newList.append(s)
            hashset[newS] = newList

        res = []
        for k, v in hashset.items():
            res.append(v)
        return res