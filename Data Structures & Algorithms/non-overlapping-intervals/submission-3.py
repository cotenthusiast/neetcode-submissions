import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])


        # [1, 2] [1, 3] [2, 5] [3, 7] [7, 8] [7, 12] [8, 11] [9, 10] [10,11] [11,12]
        #  0      1      1      0      0      1       1       0       0       0
        #    
        # [1, 2] [3, 7] [7, 8] [9, 10] [10, 11] [11, 12]


        end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                count += 1
                end = min(intervals[i][1], end)

        return count