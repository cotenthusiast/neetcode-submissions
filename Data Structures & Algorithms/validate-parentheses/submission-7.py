class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        start = "{[("
        stack = []

        for char in s:
            if char in start:
                stack.append(char)
            else:
                if len(stack) > 0 and match[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0