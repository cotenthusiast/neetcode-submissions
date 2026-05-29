class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums.sort()
        triplets = []
        if nums[i] > 0 or len(nums) < 3:
            return triplets
        while i < len(nums) - 2 and nums[i] <= 0:
            if i == 0 or nums[i] != nums[i-1]:
                fixed = i
                left = i + 1
                right = len(nums) - 1
                target = -nums[i]
                while right>left:
                    sum = nums[left] + nums[right]
                    if sum == target:
                        triplets.append([nums[fixed], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1               
                    elif sum > target:
                        right -= 1
                    else:
                        left += 1
            i += 1
        return triplets


