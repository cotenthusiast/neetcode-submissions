class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        for i, (start, _) in enumerate(intervals):
            if newInterval[0] < start: # start of the interval of the new interval is less than the current interval at index i
                insert_i = i
                break
        else:
            insert_i = len(intervals)

        
        intervals = intervals[0:insert_i] + [newInterval] + intervals[insert_i::]

        i = 1
        new_list = [intervals[0]]
        while i < len(intervals):
            if new_list[-1][1] >= intervals[i][0]:
                new_list[-1][1] = max(intervals[i][1], new_list[-1][1])
            else:
                new_list.append(intervals[i])
            i += 1

        return new_list
        