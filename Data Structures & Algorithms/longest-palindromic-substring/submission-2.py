class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 0
        res = ""

        for i in range(len(s)): # odd number case d
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tmp = s[l: r + 1]
                if len(tmp) > count:
                    res = tmp
                    count = len(tmp)
                l -= 1
                r += 1

        for i in range(len(s)): # even number case dd
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tmp = s[l : r + 1]
                if len(tmp) > count:
                    res = tmp
                    count = len(tmp)
                l -= 1
                r += 1

        return res
