class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(i, j, cache):
            if (i, j) in cache:
                return cache[(i, j)]
            distance = 0
            for dx, dy in directions:
                if 0 <= i + dx < len(matrix) and 0 <= j + dy < len(matrix[i + dx]):       # new cell within boundaries
                    if matrix[i + dx][j + dy] > matrix[i][j]:                        # new cell is greater than current one
                        if (i+dx, j+dy) in cache:
                            distance = max(distance, 1 + cache[(i+dx, j+dy)])
                        else:
                            distance = max(distance, 1 + dfs(i + dx, j + dy, cache))
            cache[(i, j)] = distance

            return distance

        directions = [(1, 0),(0, 1),(-1, 0),(0, -1)]
        cache = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                dfs(i, j, cache)

        return max(cache.values()) + 1