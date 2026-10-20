class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        new_matrix = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[j][len(matrix)-1-i] = matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = new_matrix[i][j]

        return None

        # [1, 2] [00, 01] [3, 1] [10, 00]
        # [3, 4] [10, 11] [4, 2] [11, 01]