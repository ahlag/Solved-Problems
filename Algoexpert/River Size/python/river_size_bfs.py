import unittest

def riverSizes(matrix):
    # Write your code here.
	
	row, column = len(matrix), len(matrix[0])
	visited = [[False for value in row] for row in matrix]
	river_sizes = []
	
	for i in range(row):
		for j in range(column):
			
			if visited[i][j]:
				continue

			traverseNode(i, j, matrix, visited, river_sizes)
				
	return river_sizes

def traverseNode(i, j, matrix, visited, river_sizes):

	queue = [(i, j)]
	size = 0
	
	while queue:
		
		i, j = queue.pop(0)
		
		if visited[i][j]:
			continue
			
		visited[i][j] = True
		
		if matrix[i][j] == 0:
			continue

		size += 1
		
		if i > 0 and not visited[i-1][j]:
			queue.append((i-1, j))

		if i < len(matrix) - 1 and not visited[i+1][j]:
			queue.append((i+1, j))
			
		if j > 0 and not visited[i][j-1]:
			queue.append((i, j-1))
			
		if j < len(matrix[0]) - 1 and not visited[i][j+1]:
			queue.append((i, j+1))
			
	if size > 0:
		river_sizes.append(size)
		
	return river_sizes

def test_case(self):
        testInput = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

if __name__ == "__main__":
    unittest.main()
