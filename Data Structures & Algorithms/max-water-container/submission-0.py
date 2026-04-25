class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumVolume = 0
        l, r = 0, len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            maximumVolume = max(maximumVolume, height * width)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        return maximumVolume
        