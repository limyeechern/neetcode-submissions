class Solution:
    def trap(self, height: List[int]) -> int:
        # fundamentally we need to get the minimum of left and right, subtracting the height at i
        l ,r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        volume = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                # at this point maxRight is more than equal maxLeft
                volume += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                volume += maxRight - height[r]
        return volume



