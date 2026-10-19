class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        subsequence = [[] for _ in range(len(nums))]
        
        if not nums:
            return 0
        subsequence[0] = 0


        for i in range(len(nums)):

            current_max = 0

            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    current_max = max(current_max, subsequence[j] + 1)

            subsequence[i] = current_max

        return max(subsequence) + 1