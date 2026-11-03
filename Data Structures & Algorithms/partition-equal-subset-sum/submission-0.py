class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        
        def recursive(i, remaining):
            if remaining == 0:
                return True
            if i == len(nums):
                return False
            for j in range(i, len(nums)):
                if recursive(j + 1, remaining - nums[i]):
                    return True
                if recursive(j + 1, remaining):
                    return True
            return False

        return recursive(0, sum_nums/2)