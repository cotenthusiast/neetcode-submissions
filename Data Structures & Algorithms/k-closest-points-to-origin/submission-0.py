import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            distance = self.euclideanDistance(0, points[i][0], 0, points[i][1])
            heapq.heappush(heap, (distance, i))

        ret_list = []

        for i in range(k):
            ret_list.append(points[heapq.heappop(heap)[1]])

        return ret_list

    def euclideanDistance(self, x1, x2, y1, y2):
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)
        