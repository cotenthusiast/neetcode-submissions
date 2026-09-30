from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for c in range(cols)] for r in range(rows)]
        directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]

        max_size = 0
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[r])):

                if grid[r][c] == 1 and not visited[r][c]:
                    q.append((r, c))
                    visited[r][c] = True
                    current_size = 0

                    while q:
                        current_row, current_col = q.popleft()
                        current_size += 1
                        max_size = max(max_size, current_size)

                        for d in directions:
                            dr, dc = d
                            new_row = current_row + dr
                            new_col = current_col + dc

                            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and grid[new_row][new_col] == 1:
                                q.append((new_row, new_col))
                                visited[new_row][new_col] = True

        return max_size