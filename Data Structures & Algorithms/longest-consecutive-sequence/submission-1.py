class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        starting_point = set()
        for num in nums:
            if num - 1 not in num_set:
                starting_point.add(num)
        max_len = 0
        for num in starting_point:
            current = 1
            temp = num
            while temp + 1 in num_set:
                temp += 1
                current += 1
            max_len = max(max_len, current)
        return max_len