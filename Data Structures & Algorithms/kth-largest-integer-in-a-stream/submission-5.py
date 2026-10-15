import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = [-num for num in nums]
        heapq.heapify(self.stream)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, -val)
        temp = []
        for i in range(self.k):
            current = heapq.heappop(self.stream)
            heapq.heappush(temp, current)

        ret = -current
        for i in range (self.k):
            heapq.heappush(self.stream, heapq.heappop(temp))
        return ret