class Solution:
    def numDecodings(self, s: str) -> int:
        

        # 12 10 2 3 4 _

        ans = [0] * (len(s) + 1)
        ans[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                continue
            ans[i] = ans[i + 1]
            if i + 1 < len(s):
                digit = int(s[i] + s[i+1])
                if 10 <= digit <= 26:
                    print(i)
                    ans[i] += ans[i+2]
        
        print(ans)
        return ans[0]