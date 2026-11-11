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

        # right = 2
        # left = 1
        # width = 2-1 = 1
        # area = 7 x 1

        # right = 2
        # left = 0
        # width = 2 - 0 = 2
        # area = 3 x 2

        # right = 2
        # left = -1
        # width = 2 -- 1 = 3
        # area = 1 x 3 = 3