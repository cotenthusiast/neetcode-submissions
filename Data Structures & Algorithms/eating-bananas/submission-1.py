class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left < right:
            mid = (right + left) // 2
            hours = 0
            for i in range (len(piles)):
                temp = piles[i]
                hours += temp // mid
                if temp % mid != 0:
                    hours += 1
            if hours > h:
                left = mid + 1
            elif hours <= h:
                right = mid
        return left
