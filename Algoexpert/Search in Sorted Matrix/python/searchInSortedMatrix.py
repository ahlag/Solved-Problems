import unittest

# O(n+m) time | O(1) space
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while col >= 0 and row < len(matrix):
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]

    return [-1, -1]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
        actual = searchInSortedMatrix(matrix, 44)
        self.assertEqual(actual, [3, 3])

if __name__ == "__main__":
    unittest.main()