class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        current = []
        
        def backtrack(i, current_sum):
            if current_sum == target:
                combinations.append(current.copy())
                return
            if current_sum > target or i == len(nums):
                return
            
            current.append(nums[i])
            backtrack(i, current_sum + nums[i])
            current.pop()
            
            backtrack(i + 1, current_sum)

        backtrack(0, 0)
        return combinations