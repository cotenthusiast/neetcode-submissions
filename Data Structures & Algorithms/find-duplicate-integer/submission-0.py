class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        new = 0
        while slow != fast or slow == fast == 0:
           slow = nums[slow]
           fast = nums[fast]
           fast = nums[fast]

        while new!=slow:
            slow = nums[slow]
            new = nums[new]

        return new 
