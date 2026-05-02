class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans = [0] * (len(s) + 1)
        ans[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) > len(s):
                    continue
                if s[i:i + len(w)] == w:
                    ans[i] = max(ans[i + len(w)], ans[i])
        
        print(ans)
        return ans[0] == 1