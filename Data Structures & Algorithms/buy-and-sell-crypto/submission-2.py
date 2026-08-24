class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min = prices[0]
        sum = 0
        max = 0

        for i in range (1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            else: 
                sum = prices[i] - min
                if sum > max:
                    max = sum

        return max