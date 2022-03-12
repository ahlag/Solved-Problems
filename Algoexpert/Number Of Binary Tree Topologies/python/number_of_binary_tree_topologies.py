import unittest

# Upper Bound: time O(n*(2n)!/n!(n+1)!) | space O(n)
def numberOfBinaryTreeTopologiesRecursion(n):

    if n == 0:
        return 1
    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologiesRecursion(leftTreeSize)
        numberOfRightTrees = numberOfBinaryTreeTopologiesRecursion(rightTreeSize)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees

    return numberOfTrees

# time O(n^2) | space O(n)
def numberOfBinaryTreeTopologiesMemo(n, cache={0: 1}):
	
	if n in cache:
		return cache[n]
	
	numberOfTrees = 0
	for leftTreeSize in range(n):
		rightTreeSize = n - 1 - leftTreeSize
		numberOfLeftTrees = numberOfBinaryTreeTopologiesMemo(leftTreeSize)
		numberOfRightTrees = numberOfBinaryTreeTopologiesMemo(rightTreeSize)
		numberOfTrees += numberOfLeftTrees * numberOfRightTrees
		
	cache[n] = numberOfTrees
	
	return cache[n]

# time O(n^2) | space O(n)
def numberOfBinaryTreeTopologiesOptimized(n):

    cache = [1]

    for m in range(1, n+1):
        numberOfTrees = 0
        for leftTreeSize in range(m):
            rightTreeSize = m - 1 - leftTreeSize
            numberOfLeftTrees = numberOfBinaryTreeTopologiesOptimized(leftTreeSize)
            numberOfRightTrees = numberOfBinaryTreeTopologiesOptimized(rightTreeSize)
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        cache.append(numberOfTrees)

    return cache[n]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(numberOfBinaryTreeTopologiesOptimized(3), 5)
        
    def test_case_2(self):
        self.assertEqual(numberOfBinaryTreeTopologiesMemo(3), 5)
        
    def test_case_3(self):
        self.assertEqual(numberOfBinaryTreeTopologiesRecursion(3), 5)

if __name__ == "__main__":
    unittest.main()