
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build weighted directed graph
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        # 2. Initialise shortest known distances
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # 3. Start from k
        heap = [(0, k)]

        # 4. Explore nodes in order of shortest known distance
        while heap:
            distance, node = heapq.heappop(heap)

            # Ignore outdated heap entries
            if distance > dist[node]:
                continue

            # Try every outgoing edge
            for neighbor, weight in graph[node]:
                new_distance = distance + weight

                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

        # 5. The signal must reach every node
        answer = max(dist[1:])

        return -1 if answer == float('inf') else answer
