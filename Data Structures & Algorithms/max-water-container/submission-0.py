class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highestArea = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            length = right - left
            if heights[left] < heights[right]:
                highestArea = max(length * heights[left], highestArea)
                left += 1
            else:
                highestArea = max(length * heights[right], highestArea)
                right -= 1
        return highestArea