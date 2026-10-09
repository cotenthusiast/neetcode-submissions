import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        heap = []
        for task in tasks:
            if task in hashmap:
                hashmap[task]+=1
            else:
                hashmap[task] = 1
        for task, count in hashmap.items():
            heapq.heappush(heap, (-count, task))

        cooldown = deque()
        time = 0

        while heap or cooldown:
            if cooldown and time >= cooldown[0][2]:
                next_item = cooldown.popleft()
                heapq.heappush(heap, (next_item[0], next_item[1])) 
            if heap:
                highest_priority = heapq.heappop(heap)
                if highest_priority[0] + 1 < 0:
                    cooldown.append((highest_priority[0]+1, highest_priority[1], time + n+1))
            time += 1
        return time



