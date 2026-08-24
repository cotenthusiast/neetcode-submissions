class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Rows
        for row in range(9):
            if not self.check(board[row]):
                return False

        # Columns
        for col in range(9):
            values = [board[row][col] for row in range(9)]

            if not self.check(values):
                return False

        # 3x3 sub-boxes
        for i in range(9):
            start_row = (i // 3) * 3
            start_col = (i % 3) * 3

            values = []

            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    values.append(board[row][col])

            if not self.check(values):
                return False

        return True

    def check(self, values):
        values = [value for value in values if value != "."]
        return len(set(values)) == len(values)