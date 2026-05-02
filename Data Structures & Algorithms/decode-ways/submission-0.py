class Solution:
    def numDecodings(self, s: str) -> int:
        ans = [0] * (len(s) + 1)
        ans[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] != "0":
                ans[i] = ans[i + 1] 
            if i + 1 < len(s):
                digit = int(s[i] + s[i + 1])
                if digit <= 26 and digit >= 10:
                    ans[i] += ans[i + 2]
        
        return ans[0]