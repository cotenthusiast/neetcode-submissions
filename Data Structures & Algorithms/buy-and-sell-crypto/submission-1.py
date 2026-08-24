class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = -1
        max = 0
        running_sum = 0

        while current < len(prices) - 1:
            current += 1
            future = current + 1
            while future < len(prices):
                running_sum = prices[future] - prices[current]
                if running_sum > max:
                    max = running_sum
                future += 1
            
        return max
