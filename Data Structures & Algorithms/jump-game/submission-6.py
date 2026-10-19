class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reach = nums[0]
        for i in range(1, len(nums)):
            current_reach = nums[i] + i
            if max_reach < i:
                return False
            max_reach = max(max_reach, current_reach) 
        return True           
