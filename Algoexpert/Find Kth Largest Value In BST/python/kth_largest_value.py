import unittest

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class TreeInfo:
	def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
		self.numberOfNodesVisited = numberOfNodesVisited
		self.latestVisitedNodeValue = latestVisitedNodeValue

def findKthLargestValueInBstReverse(tree, k):

    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
	if node is None or treeInfo.numberOfNodesVisited >= k:
		return
	
	reverseInOrderTraverse(node.right, k, treeInfo)
	if treeInfo.numberOfNodesVisited < k:
		treeInfo.numberOfNodesVisited += 1
		treeInfo.latestVisitedNodeValue = node.value
		reverseInOrderTraverse(node.left, k, treeInfo)

# time O(n) | space O(n)
def findKthLargestValueInBstRecursion(tree, k):
    sortedNodeValues = []
    inOrderTraverse(tree, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues) - k]

def inOrderTraverse(node, sortedNodeValues):
    if node is None:
        return
    
    inOrderTraverse(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraverse(node.right, sortedNodeValues)
    
# time O(h) | space O(n)
def findKthLargestValueInBstRecursion(tree, k):
    sortedNodeValues = []
    inOrderTraverse(tree, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues) - k]

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(15)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.left.right = BST(3)
        root.left.right = BST(5)
        root.right = BST(20)
        root.right.left = BST(17)
        root.right.right = BST(22)
        k = 3
        expected = 17
        actual = findKthLargestValueInBstRecursion(root, k)
        self.assertEqual(actual, expected)
        
    def test_case_2(self):
        root = BST(15)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.left.right = BST(3)
        root.left.right = BST(5)
        root.right = BST(20)
        root.right.left = BST(17)
        root.right.right = BST(22)
        k = 3
        expected = 17
        actual = findKthLargestValueInBstReverse(root, k)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()