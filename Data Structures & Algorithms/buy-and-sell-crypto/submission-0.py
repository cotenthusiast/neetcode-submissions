class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        current = prices[0]
        total = 0
        temp = 0
        for i in range(1, len(prices)):
            if prices[i] < current:
                current = prices[i]
            else:
                temp = prices[i] - current
                if temp>total:
                    total = temp
        return total
