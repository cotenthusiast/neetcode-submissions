class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range (0, len(nums)):
            lookup[nums[i]] = i
        for i in range (0, len(nums)):
            current_target = target - nums[i]
            if current_target in lookup and i != lookup[current_target]:
                return [i, lookup[current_target]]
