class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = 0
        while l < r:
            minHeight = min(height[l], height[r])
            water = minHeight * (r - l)
            maxWater = max(maxWater, water)
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        return maxWater
