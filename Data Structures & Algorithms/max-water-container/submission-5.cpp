#include <algorithm>

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int area = 0;
        int max_area = -1;
        while (left < right) {
            area = std::min(heights[left], heights[right]) * (right - left);
            if (area > max_area) { 
                max_area = area;
            }
            if (heights[left] > heights[right]) {
                right --;
            } else {
                left ++;
            }
        }
        return max_area;
    }
};
