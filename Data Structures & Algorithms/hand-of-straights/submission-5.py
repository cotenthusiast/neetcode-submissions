import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        min_heap = hand.copy()
        heapq.heapify(min_heap)
        length = len(hand)
        base_index = 0
        groups = []
        previous = -1
        for i in range(length):
            card = heapq.heappop(min_heap)
            if not (card == previous):
                offset = 0

            while base_index + offset < len(groups) and card - 1 != groups[base_index + offset][-1]:
                offset += 1
                


            if base_index + offset == len(groups):
                groups.append([(card)])
            else:
                groups[base_index + offset].append(card)
                if len(groups[base_index+offset]) == groupSize:
                    base_index += 1
            previous = card

        length = groupSize

        for group in groups:
            length = min(length, len(group))
                 
        return length == groupSize