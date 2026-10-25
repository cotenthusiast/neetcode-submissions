from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque() 
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:

            i, j, distance = q.popleft()
            grid[i][j] = distance

            for dx, dy in directions:

                new_i = i + dx
                new_j = j + dy

                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] != -1 and grid[new_i][new_j] != 0 and distance + 1 < grid[new_i][new_j]:

                    grid[new_i][new_j] = distance + 1
                    q.append((new_i, new_j, distance + 1))
