class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = -1
        up = -1
        right = len(matrix[0])
        down = len(matrix)
        output = []
        while len(output) < len(matrix) * len(matrix[0]):

            for i in range(left + 1, right):
                output.append(matrix[up+1][i])

            for i in range(up + 2, down):
                output.append(matrix[i][right-1]) 

            if len(output) == len(matrix) * len(matrix[0]):
                break
            for i in range(right - 2, left, -1):
                output.append(matrix[down-1][i])

            if len(output) == len(matrix) * len(matrix[0]):
                break
            for i in range(down - 2, up + 1, -1):
                output.append(matrix[i][left + 1])

            left += 1
            right -= 1
            up += 1
            down -=1

        return output