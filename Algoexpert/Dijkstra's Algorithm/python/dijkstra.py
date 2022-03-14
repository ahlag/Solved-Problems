import unittest

# O(v^2 + e) time | O(v) - where v is the number of
# vertices and e is the number of edges in the input graph
def dijkstrasAlgorithmArray(start, edges):
    
	numberOfVertices = len(edges)
    
	minDistances = [float('inf') for _ in range(numberOfVertices)]
	minDistances[start] = 0
	
	visited = set()
	
	while len(visited) != numberOfVertices:
		vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)
		
		if currentMinDistance == float('inf'):
			break
		
		visited.add(vertex)
		
		for edge in edges[vertex]:
			destination, distanceToDestination = edge
			
			if destination in visited:
				continue
				
			newPathDistance = currentMinDistance + distanceToDestination
			currentDestinationDistance = minDistances[destination]
			if newPathDistance < currentDestinationDistance:
				minDistances[destination] = newPathDistance
	
	return list(map(lambda x: -1 if x == float('inf') else x, minDistances))

def getVertexWithMinDistance(distance, visited):
	
	currentMinDistance = float('inf')
	vertex = -1
	
	for vertexIdx, distance in enumerate(distance):
		if vertexIdx in visited:
			continue
			
		if distance <= currentMinDistance:
			vertex = vertexIdx
			currentMinDistance = distance
			
	return vertex, currentMinDistance

# O((v + e) * log(v) time | O(v) - where v is the number of
# vertices and e is the number of edges in the input graph
def dijkstrasAlgorithmHeap(start, edges):
    
	numberOfVertices = len(edges)
    
	minDistances = [float('inf') for _ in range(numberOfVertices)]
	minDistances[start] = 0
	
	minDistancesHeap = MinHeap([(idx, float('inf')) for idx in range(numberOfVertices)])
	minDistancesHeap.update(start, 0)
	
	while not minDistancesHeap.isEmpty():
		vertex, currentMinDistance = minDistancesHeap.remove()
		
		if currentMinDistance == float('inf'):
			break
		
		for edge in edges[vertex]:
			destination, distanceToDestination = edge
				
			newPathDistance = currentMinDistance + distanceToDestination
			currentDestinationDistance = minDistances[destination]
			if newPathDistance < currentDestinationDistance:
				minDistances[destination] = newPathDistance
				minDistancesHeap.update(destination, newPathDistance)
	
	return list(map(lambda x: -1 if x == float('inf') else x, minDistances))

class MinHeap:

	def __init__(self, array):
		# Do not edit the line below.
		self.vertexMap = {idx: idx for idx in range(len(array))}
		self.heap = self.buildHeap(array)

	def isEmpty(self):
		return len(self.heap) == 0

	# O(N) time and O(1) space
	def buildHeap(self, array):
		# Write your code here.
		firstParent = (len(array) - 2) // 2
		for currentIndex in reversed(range(firstParent + 1)):
			self.siftDown(currentIndex, len(array) - 1, array)
			#print(array)
		return array

	# O(log(n)) time and O(1) space
	def siftDown(self, start, endIdx, heap):
		# Write your code here.
		childOneIdx = start * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = start * 2 + 2 if start * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap][1] < heap[start][1]:
				self.swap(start, idxToSwap, heap)
				start = idxToSwap
				childOneIdx = start * 2 + 1
			else:
				return
		
	# O(log(n)) time and O(1) space
	def siftUp(self, start, heap):
		# Write your code here.
		parentIdx = (start - 1) // 2
		while start > 0 and heap[start][1] < heap[parentIdx][1]:
			self.swap(start, parentIdx, heap)
			start = parentIdx
			parentIdx = (start - 1) // 2
			
	def swap(self, i, j, array):
		self.vertexMap[array[i][0]] = j
		self.vertexMap[array[j][0]] = i
		array[i], array[j] = array[j], array[i]

	# O(log(n)) time and O(1) space
	def remove(self):
		# Write your code here.
		self.swap(0, len(self.heap) - 1, self.heap)
		vertex, distance = self.heap.pop()
		self.vertexMap.pop(vertex)
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return vertex, distance

	def update(self, vertex, value):
		self.heap[self.vertexMap[vertex]] = (vertex, value)
		self.siftUp(self.vertexMap[vertex], self.heap)
		


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        start = 0
        edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
        expected = [0, 7, 13, 27, 10, -1]
        actual = dijkstrasAlgorithmHeap(start, edges)
        self.assertEqual(actual, expected)
        
    def test_case_2(self):
        start = 0
        edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
        expected = [0, 7, 13, 27, 10, -1]
        actual = dijkstrasAlgorithmArray(start, edges)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()