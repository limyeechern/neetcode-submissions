class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(i, curr):
            if i >= len(digits):
                res.append(curr)
                return
            digit = digits[i]
            chars = digitMap[digit]
            for j in range(len(chars)):
                dfs(i + 1, curr + chars[j])

        dfs(0, '')
        print(res)
        return res