from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:
            return [nums[0]]

        maxes = []
        max_queue = deque()
        time = 1
        max_queue.append([nums[0],k])

        for i in range(1, k):
            if nums[i] > max_queue[0][0]:
                max_queue = deque()
                max_queue.append([nums[i], time + k])
            else:
                while nums[i] > max_queue[-1][0]:
                    max_queue.pop()
                max_queue.append([nums[i], time + k])
            time += 1
        maxes.append(max_queue[0][0])

        for i in range(k, len(nums)):
            if max_queue[0][1] == time:
                max_queue.popleft()
            if not max_queue or nums[i] > max_queue[0][0]:
                max_queue = deque()
                max_queue.append([nums[i], time + k])
            else:
                while nums[i] > max_queue[-1][0]:
                    max_queue.pop()
                max_queue.append([nums[i], time + k])
            time += 1
            maxes.append(max_queue[0][0])

        return maxes