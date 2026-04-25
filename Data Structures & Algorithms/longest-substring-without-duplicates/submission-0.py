class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyxyzyz"
        window = set()
        count = 0
        l = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            count = max(count, r - l + 1)
        return count
            
