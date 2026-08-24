class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        end = "}])"
        start = "{[("
        stack = []

        for i in range (len(s)):
            char = s[0]
            s = s[1:]
            if char in start:
                stack.append(char)
            else:
                if len(stack) > 0 and match[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        



