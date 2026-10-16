class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i):
            if i == len(nums):
                subsets.append(current.copy())
                return
            
            current.append(nums[i])
            backtrack(i + 1)
            
            current.pop()
            backtrack(i+1)

        subsets = []
        current = []
        backtrack(i = 0)
        return subsets

