# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
        # bank = "("*n + ")"*n
        # current = bank[0] + bank[-1]
        # bank = bank[1:len(bank)-1]

        # lists = []

        # def backtrack(current, bank):
        #     if not bank:
        #         lists.append(current)
        #         return
        #     backtrack(current[0] + bank[0] + current[-1], bank[1:len(bank)])
        #     backtrack(current[0] + current+bank[-1] + current[-1], bank[0:len(bank)-1])

        # backtrack(current, bank)

        # return lists

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, opened, closed):
            if len(current) == 2 * n:
                result.append(current)
                return

            if opened < n:
                backtrack(current + "(", opened + 1, closed)

            if closed < opened:
                backtrack(current + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return result