class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, remaining):
            if remaining == 0:
                return 1                      # found one valid combination
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            count = 0
            for j in range(i, len(coins)):    # only coins from index i onwards
                coin = coins[j]
                if remaining - coin < 0:
                    continue
                count += dfs(j, remaining - coin)   # pass j, not 0 → can reuse coin j, never go back

            memo[(i, remaining)] = count
            return count

        return dfs(0, amount)