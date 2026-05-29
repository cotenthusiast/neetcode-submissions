class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = []
        product_before = [1]
        product_after = [1]
        for i in range (1,len(nums)):
            product_before.append(nums[i-1]*product_before[i-1])
        for i in range (1,len(nums)):
            product_after.append(nums[len(nums)-i]*product_after[i-1])
        product_after.reverse()
        for i in range (0, len(nums)):
            answers.append(product_before[i] * product_after[i])
        return answers            