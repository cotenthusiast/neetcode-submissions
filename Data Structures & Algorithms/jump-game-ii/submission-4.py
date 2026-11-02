class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        reach = nums[0]
        candidate_reach = 0
        jumps = 1

        for i in range(1, len(nums)):
            if reach >= len(nums) - 1:
                return jumps
            if reach == i:
                reach = max(candidate_reach, i + nums[i])
                jumps += 1
            else:
                candidate_reach = max(candidate_reach, i + nums[i])
            

        return jumps