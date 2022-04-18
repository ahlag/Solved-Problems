import unittest

# O(n) time | O(n) space
def hasSingleCycleBitArray(array):

	n = len(array)
	visited = [0] * n
	curIndex = 0

	for _ in range(n):
		
		# graph traversal
		nextIndex = (curIndex + array[curIndex]) % n
		visited[nextIndex] = 1
		curIndex = nextIndex
	
	return sum(visited) == n

# O(n) time | O(1) space
def hasSingleCycleBitVector(array):

	n = len(array)
	visited = 0
	curIndex = 0

	for _ in range(n):
		
		# graph traversal
		nextIndex = (curIndex + array[curIndex]) % n
		visited = visited | 1 << nextIndex
		curIndex = nextIndex

	return visited + 1 == 2 ** n

# O(n) time | O(1) space
def hasSingleCycle(array):
    
    numElementsVisited = 0
    currentIdx = 0
    
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
        
    return currentIdx == 0

def getNextIdx(currentIdx, array):

    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 908, -26]), True)
        self.assertEqual(hasSingleCycleBitArray([10, 11, -6, -23, -2, 3, 88, 908, -26]), True)
        self.assertEqual(hasSingleCycleBitVector([10, 11, -6, -23, -2, 3, 88, 908, -26]), True)

if __name__ == "__main__":
    unittest.main()
