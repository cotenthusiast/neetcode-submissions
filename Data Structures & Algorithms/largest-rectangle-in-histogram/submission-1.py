class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        stack = [0]
        area = 0

        for i in range(1, len(heights)):
            if heights[stack[-1]] > heights[i]:
                right = stack[-1]
                while stack and heights[stack[-1]] > heights[i]:
                    index = stack.pop()
                    left = stack[-1] if stack else -1
                    width = right - left
                    area = max(area, width * heights[index])

            stack.append(i)

        right = stack[-1]
        while stack:
                index = stack.pop()
                left = stack[-1] if stack else -1
                width = right - left
                area = max(area, width * heights[index])

        return area