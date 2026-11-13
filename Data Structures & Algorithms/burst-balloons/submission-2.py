class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        def dfs(left, right):
            if (left, right) in cache:
                return cache[(left, right)]
            if left + 1 == right:
                return 0
            
            maximum = 0
            for i in range(left + 1, right):
                maximum = max(maximum, nums[left] * nums[i] * nums[right] + dfs(left, i) + dfs(i, right))
            

            cache[(left, right)] = maximum
            return maximum

        nums = [1] + nums + [1]
        cache = {}
        return dfs(0, len(nums)-1)