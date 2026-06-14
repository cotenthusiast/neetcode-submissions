class Solution:
    def binary_search(self, target: int, array: List[int]) -> int:
        left = 0
        right = len(array) - 1

        while left <= right:
            mid = (left + right) // 2

            if array[mid] > target:
                right = mid - 1
            elif array[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        min_index = left

        array1 = nums[0:min_index]
        array2 = nums[min_index:]

        result = self.binary_search(target, array1)
        if result != -1:
            return result  

        result = self.binary_search(target, array2)
        return result + min_index if result != -1 else -1