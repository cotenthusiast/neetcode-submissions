class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def add_col(danger, i):
            for y in range(n):
                danger.add((i, y))
            return danger
        
        def add_diagonal(danger, i, j):
            left = i
            right = i
            y = j
            while left >= 0 or right < n:
                if left>=0:
                    danger.add((left, y))
                    left -= 1
                if right < n:
                    danger.add((right, y))
                    right += 1
                y += 1
            return danger

        def update_danger(danger, i, j):
            danger = add_col(danger, i)
            danger = add_diagonal(danger, i, j)
            return danger

        def backtrack(current, danger, j):
            if j == n:
                if len(current) == n:
                    valid_setups.append(current.copy())
                return
            for i in range(n):
                if (i, j) in danger:
                    continue
                current.append("."*i + "Q" + "."*(n-i-1))
                backtrack(current, update_danger(danger.copy(), i, j), j + 1)
                current.pop()
                
        current = []
        valid_setups = []
        danger = set()
        backtrack(current, danger, 0)

        return valid_setups


