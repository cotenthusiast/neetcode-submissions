class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numletter = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz", 
        }

        def backtrack(i, current):
            if i == len(digits):
                array.append(current)
                return
            for c in numletter[int(digits[i])]:
                backtrack(i + 1, current + c)
        
        if not digits:
            return []

        array = []
        backtrack(0, "")

        return array