class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        holding = -prices[0]
        cooldown = 0
        free = 0

        for i in range(1, len(prices)):
            prev_h, prev_c, prev_f = holding, cooldown, free
            cooldown = prev_h + prices[i]
            holding = max(prev_h, prev_f-prices[i])
            free = max(prev_f, prev_c)


        return max(free, cooldown)