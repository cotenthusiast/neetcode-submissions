import math
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def distance(point1: List[int], point2: List[int]) -> int:
            return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

        network = [points[0]]
        points = points[1::]

        total_distance = 0
        visited = [network[0]]
        len_points = len(points)
        distances = []
        for i in range(len_points):
            for point_outside in points:
                heapq.heappush(distances, (distance(network[i], point_outside), point_outside))
            while True:
                min_distance, point = heapq.heappop(distances)

                if point not in visited:
                    break
            
            network.append(point)
            total_distance += min_distance
            visited.append(point)
            points.remove(point)
        
        return total_distance
