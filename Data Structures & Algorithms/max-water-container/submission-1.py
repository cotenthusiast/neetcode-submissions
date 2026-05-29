class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while right>left:
            if (right-left) * min(heights[right], heights[left])>max_area:
                max_area = (right-left) * min(heights[right], heights[left])
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_area