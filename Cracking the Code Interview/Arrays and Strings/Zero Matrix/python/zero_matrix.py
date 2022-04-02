# O(MxN)
import unittest
from copy import deepcopy

def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix

def set_zeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    row, col = len(matrix), len(matrix[0])
    
    vertical = [False] * row
    horizontal = [False] * col
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                vertical[i] = True
                horizontal[j] = True

    for i in range(row):
        for j in range(col):
            if vertical[i] is True or horizontal[j] is True:
                matrix[i][j] = 0
                
    return matrix

class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    testable_functions = [
        zero_matrix, 
        # zero_matrix_pythonic
        set_zeroes
    ]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()