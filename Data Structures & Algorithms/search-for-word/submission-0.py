class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]
        allowed = [
            (r, c)
            for r in range(len(board))
            for c in range(len(board[r]))
        ]
        nono_square = []

        def backtrack(i, nono_square):
            nonlocal allowed
            if i == len(word): # only way to reach this far is by actually reaching the last letter
                return True
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if (r, c) in allowed and (r, c) not in nono_square and board[r][c] == word[i]:
                        temp = allowed.copy()
                        allowed = [(r + dr, c + dc) for dr, dc in directions]
                        nono_square.append((r, c))
                        if backtrack(i+1, nono_square):
                            return True
                        else:
                            allowed = temp
                            nono_square.pop()
            return False
        
        return backtrack(0, nono_square)