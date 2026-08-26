class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in lookup:
                return [min(lookup[needed], i), max(lookup[needed], i)]

            lookup[nums[i]] = i
