class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = len(digits) - 1
        while digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits = [1] + digits
                break
            i -= 1
            digits[i] += 1
        return digits