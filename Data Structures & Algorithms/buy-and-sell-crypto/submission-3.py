class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max = 0

        for i in range(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            else:
                sum = prices[i] - lowest_price
                if sum > max:
                    max = sum
        return max
