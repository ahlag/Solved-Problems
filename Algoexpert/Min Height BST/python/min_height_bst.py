import unittest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

# O(nlog(n)) time | O(n) space
def minHeightBstInsert(array):
    return constructMinHeightBstInsert(array, None, 0, len(array)-1)

def constructMinHeightBstInsert(array, bst, startIdx, endIdx):
	if startIdx > endIdx:
		return
	
	midIdx = (startIdx + endIdx) // 2
	valueToAdd = array[midIdx]
	
	if bst is None:
		bst = BST(valueToAdd)
	else:
		bst.insert(valueToAdd)

	constructMinHeightBstInsert(array, bst, startIdx, midIdx-1)
	constructMinHeightBstInsert(array, bst, midIdx+1, endIdx)
	return bst

# O(n) time | O(n) space
def minHeightBstRecursive(array):
    return constructMinHeightBstRecursive(array, None, 0, len(array)-1)

def constructMinHeightBstRecursive(array, bst, startIdx, endIdx):
    if startIdx > endIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    newBstNode = BST(array[midIdx])

    if bst is None:
        bst = newBstNode
    else:
        if array[midIdx] < bst.value:
            bst.left = newBstNode
            bst = bst.left
        else:
            bst.right = newBstNode
            bst = bst.right

    constructMinHeightBstRecursive(array, bst, startIdx, midIdx-1)
    constructMinHeightBstRecursive(array, bst, midIdx+1, endIdx)
    return bst

# O(n) time | O(n) space
def minHeightBstCleanRecursive(array):
    return constructMinHeightBstCleanRecursive(array, 0, len(array)-1)

def constructMinHeightBstCleanRecursive(array, startIdx, endIdx):
    if startIdx > endIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])

    bst.left = constructMinHeightBstCleanRecursive(array, startIdx, midIdx-1)
    bst.right = constructMinHeightBstCleanRecursive(array, midIdx+1, endIdx)
    return bst

## Test
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = minHeightBstInsert(array)

        self.assertTrue(validateBst(tree))
        self.assertEqual(getTreeHeight(tree), 4)

        inOrder = inOrderTraverse(tree, [])

        self.assertEqual(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])
        
    def test_case_2(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = minHeightBstRecursive(array)

        self.assertTrue(validateBst(tree))
        self.assertEqual(getTreeHeight(tree), 4)

        inOrder = inOrderTraverse(tree, [])

        self.assertEqual(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])
        
    def test_case_3(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = minHeightBstCleanRecursive(array)

        self.assertTrue(validateBst(tree))
        self.assertEqual(getTreeHeight(tree), 4)

        inOrder = inOrderTraverse(tree, [])

        self.assertEqual(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])


if __name__ == "__main__":
    unittest.main()
