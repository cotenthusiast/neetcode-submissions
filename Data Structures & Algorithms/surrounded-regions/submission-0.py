from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        verified = set()

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == 'O' and (r, c) not in verified:

                    q = deque([(r, c)])
                    temp = {(r, c)}

                    touches_border = False

                    while q:
                        current_r, current_c = q.popleft()

                        # If any cell in this component is on the edge,
                        # this component cannot be captured
                        if (
                            current_r == 0
                            or current_r == rows - 1
                            or current_c == 0
                            or current_c == cols - 1
                        ):
                            touches_border = True

                        for dr, dc in directions:
                            new_r = current_r + dr
                            new_c = current_c + dc

                            if (
                                0 <= new_r < rows
                                and 0 <= new_c < cols
                                and board[new_r][new_c] == 'O'
                                and (new_r, new_c) not in temp
                            ):
                                temp.add((new_r, new_c))
                                q.append((new_r, new_c))

                    if touches_border:
                        verified.update(temp)
                    else:
                        for row, col in temp:
                            board[row][col] = 'X'