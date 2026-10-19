from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # [1][1][1][1][1][1]|
        # [1][2][3][4][5][6] m
        # [1][3][6][10][15][21] |
        # ---- n----




        # def has_options(point: Tuple(int), m : int, n: int) -> bool:
        #     return point[0] + 1 < n and point[1] + 1 < m

        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        # directions = [(0, 1), (1, 0)]


        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
        # q = deque()
        # q.append((0, 0))

        # unique_paths = 1

        # while q:
        #     point = q.popleft()

        #     if has_options(point, m, n):
        #         unique_paths += 1

        #     for dx, dy in directions:
        #         if point[0] + dx < n and point[1] + dy < m and has_options(point, m, n):
        #             q.append((point[0] + dx, point[1] + dy)) 
        
        # return unique_paths

