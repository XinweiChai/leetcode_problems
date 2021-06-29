from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)
        c = len(matrix[0])
        self.sum_mat = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                self.sum_mat[i][j] += self.sum_mat[i - 1][j] + self.sum_mat[i][j - 1] + matrix[i - 1][j - 1] - \
                                      self.sum_mat[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_mat[row2 + 1][col2 + 1] - self.sum_mat[row2 + 1][col1] - self.sum_mat[row1][col2 + 1] + \
               self.sum_mat[row1][col1]


if __name__ == '__main__':
    # Your NumMatrix object will be instantiated and called as such:
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    row1, col1, row2, col2 = [2, 1, 4, 3]
    param_1 = obj.sumRegion(row1, col1, row2, col2)
    print(param_1)
