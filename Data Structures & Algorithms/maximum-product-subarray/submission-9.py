class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        smallest = nums[0]
        largest = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if smallest is None:
                smallest = num
                largest = num
                max_product = max(max_product, num)
                continue
            if num == 0:
                smallest = None
                largest = None
                max_product = max(max_product, 0)
                continue
            prev_largest = largest
            largest = max(num, num * largest, num * smallest)
            smallest = min(num, num * smallest, num * prev_largest)
            max_product = max(largest, smallest, max_product)

        return max_product
                
                
