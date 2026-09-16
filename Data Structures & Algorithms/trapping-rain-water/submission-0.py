class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        total_water = 0
        while left < right:

            if left_max > right_max:
                if height[right - 1] > right_max:
                    right_max = height[right - 1]
                else:
                    total_water += right_max - height[right - 1]
                right -= 1
            else:
                if height[left + 1] > left_max:
                    left_max = height[left + 1]
                else:
                    total_water += left_max - height[left + 1]
                left += 1

        return total_water