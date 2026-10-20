"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        heap = []

        intervals.sort(key = lambda x: x.start)

        heapq.heappush(heap, intervals[0].end)

        rooms = 1
        for i in range(1, len(intervals)):

            if heap[0] > intervals[i].start:
                rooms += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)

        return len(heap) 