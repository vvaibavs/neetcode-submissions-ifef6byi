class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max = 0
        while left < right:
            total = min(heights[left], heights[right]) * (right - left)
            if total > max:
                max = total
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max