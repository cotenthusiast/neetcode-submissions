from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        q = deque()

        starting_points = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(rows):
            for c in range(cols):
                if not starting_points[r][c]:

                    q.append((r, c))
                    visited = {(r, c)}

                    is_atlantic = False
                    is_pacific = False

                    while q:
                        current_row, current_col = q.popleft()

                        for dr, dc in directions:
                            new_row = current_row + dr
                            new_col = current_col + dc

                            if new_row == rows or new_col == cols:
                                is_atlantic = True

                            if new_row == -1 or new_col == -1:
                                is_pacific = True

                            if (
                                0 <= new_row < rows
                                and 0 <= new_col < cols
                                and (new_row, new_col) not in visited
                                and heights[current_row][current_col] >= heights[new_row][new_col]
                            ):
                                visited.add((new_row, new_col))
                                q.append((new_row, new_col))

                    if is_atlantic and is_pacific:
                        starting_points[r][c] = True

        ret_array = []

        for r in range(rows):
            for c in range(cols):
                if starting_points[r][c]:
                    ret_array.append([r, c])

        return ret_array