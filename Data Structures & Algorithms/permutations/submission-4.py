class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        current = []
        def backtrack(i):
            if i == len(nums):
                permutations.append(current.copy())
                return
            remaining = list(set(nums).difference(current))
            for j in range(len(remaining)):
                current.append(remaining[j])
                backtrack(i + 1)
                current.pop()
            
        backtrack(0)
        return permutations
