class Solution:

    def apply_operator(self, stack, symbol):
        right = stack.pop()
        left = stack.pop()

        if symbol == "+":
            result = left + right
        elif symbol == "-":
            result = left - right
        elif symbol == "*":
            result = left * right
        else:
            result = int(left / right)

        stack.append(result)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []

        for token in tokens:
            if token in operators:
                self.apply_operator(stack, token)
            else:
                stack.append(int(token))

        return stack.pop()