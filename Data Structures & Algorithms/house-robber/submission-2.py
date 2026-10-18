class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        totals = [nums[0], max(nums[0], nums[1]), max(nums[0] + nums[2], nums[1])]
        for i in range (3, len(nums)):
            totals.append(max(nums[i] + totals[i-2], nums[i] + totals[i-3]))
        return max(totals[-1], totals[len(totals) - 2])


