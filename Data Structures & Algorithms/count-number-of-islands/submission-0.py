from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        n_islands = 0

        rows = len(grid)
        cols = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and not visited[r][c]:
                    n_islands += 1
                    visited[r][c] = True

                    q.append((r, c))

                    while q:
                        current_row, current_col = q.popleft()
                        for d in directions:
                            dr, dc = d
                            new_row = current_row + dr
                            new_col = current_col + dc
                            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1" and not visited[new_row][new_col]:
                                visited[new_row][new_col] = True
                                q.append((new_row, new_col))

        return n_islands