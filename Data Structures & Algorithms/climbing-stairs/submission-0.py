class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}

        def ways(n):
            if n in cache:
                return cache[n]

            cache[n] = ways(n - 1) + ways(n - 2)
            return cache[n]

        return ways(n)
