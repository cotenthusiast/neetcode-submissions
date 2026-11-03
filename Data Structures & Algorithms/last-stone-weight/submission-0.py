import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            bigger_stone = -heapq.heappop(heap)
            smaller_stone = -heapq.heappop(heap)
            difference = bigger_stone - smaller_stone
            if difference > 0:
                heapq.heappush(heap, -difference)
        
        if heap:
            return -heap[0]
        else:
            return 0