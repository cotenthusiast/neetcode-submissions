class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        count = 0
        cache = {}
        def backtrack(i, total):
            paths = 0
            if (i, total) in cache:
                return cache[(i, total)]

            if i == len(nums):
                if total == target:
                    paths += 1
                cache[(i, total)] = paths
                return paths
            paths =  backtrack(i + 1, total-nums[i]) +  backtrack(i + 1, total+nums[i])
            cache[(i, total)] = paths
            return paths
        
        return backtrack(0, 0)