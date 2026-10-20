class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        new_list = [intervals[0]]
        i = 1

        while i < len(intervals):

            if new_list[-1][1] >= intervals[i][0]:
                new_list[-1][1] = max(intervals[i][1], new_list[-1][1])
            else:
                new_list.append(intervals[i])
            i += 1
        
        return new_list