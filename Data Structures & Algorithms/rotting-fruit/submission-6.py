from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        rotten = False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r, c, 0)) # gathering starting points
                    rotten = True

        while q:
            current_row, current_col, t = q.popleft()
            for d in directions:
                dr, dc = d
                new_row = current_row + dr
                new_col = current_col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col, t+1))
                
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                   return -1

        if not rotten:
            return 0

        return t