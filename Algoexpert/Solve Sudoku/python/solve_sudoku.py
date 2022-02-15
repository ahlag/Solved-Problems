import unittest

# O(1) time | O(1) space - assuming a 9x9 input board
def solveSudoku(board):
    solvePartialSudoku(0, 0, board)
    return board

def solvePartialSudoku(row, col, board):
    currentRow = row
    currentCol = col

    if currentCol == len(board[currentRow]):
        currentRow += 1
        currentCol = 0
        if currentRow == len(board):
            return True # board is completed

    if board[currentRow][currentCol] == 0:
        return tryDigitsAtPosition(currentRow, currentCol, board)

    return solvePartialSudoku(currentRow, currentCol + 1, board)

def tryDigitsAtPosition(row, col, board):
    for digit in range(1, 10):
        if isValidAtPosition(digit, row, col, board):
            board[row][col] = digit
            if solvePartialSudoku(row, col+1, board):
                return True

    board[row][col] = 0
    return False

def isValidAtPosition(value, row, col, board):
	rowIsValid = value not in board[row]
	columnIsValid = value not in map(lambda r: r[col], board)
	
	if not rowIsValid or not columnIsValid:
		return False
	
	# Check subgrid constraint
	subgridRowStart = (row//3) * 3
	subgridColStart = (col//3) * 3
	for rowIdx in range(3):
		for colIdx in range(3):
			rowToCheck = subgridRowStart + rowIdx
			colToCheck = subgridColStart + colIdx
			existingValue = board[rowToCheck][colToCheck]
			
			if existingValue == value:
				return False
	
	return True

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7],
        ]
        expected = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7],
        ]
        actual = solveSudoku(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
