class Solution:
    def numDecodings(self, s: str) -> int:
        ans = [0] * (len(s) + 1)
        ans[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                ans[i] = 0
                continue
            ans[i] = ans[i+1]
            if i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                ans[i] += ans[i + 2]
        print(ans)

        return ans[0]
