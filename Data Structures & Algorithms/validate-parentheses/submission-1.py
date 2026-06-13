class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', '}': '{', ']': '['}
        stack_opening = []

        if len(s) % 2 != 0:
            return False

        for item in s:
            if item in matching:
                if not stack_opening or matching[item] != stack_opening[-1]:
                    return False
                stack_opening.pop()
            else:
                stack_opening.append(item)

        return len(stack_opening) == 0