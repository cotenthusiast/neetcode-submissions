class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        if amount < min(coins):
            return -1 

        cache = [-1 for i in range(amount+1)]
        cache[0] = 0   

        for i in range(amount+1):
            for coin in coins:
                target = i - coin
                if target < 0 or cache[target] == -1:
                    continue
                if cache[i] == -1:
                    cache[i] = cache[target] + 1
                elif cache[i] > cache[target] + 1:
                    cache[i] = cache[target] + 1

        return cache[-1]

