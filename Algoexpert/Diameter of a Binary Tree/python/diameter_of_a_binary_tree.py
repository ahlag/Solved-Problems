import unittest

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self):
		self.diameter = 0

def binaryTreeDiameter(tree):
	treeInfo = TreeInfo()
	binaryTreeDiameterHelper(tree, treeInfo)
	return treeInfo.diameter
    
	
def binaryTreeDiameterHelper(tree, treeInfo):
	
	if tree is None:
		return 0
	
	leftHeight = binaryTreeDiameterHelper(tree.left, treeInfo)
	rightHeight = binaryTreeDiameterHelper(tree.right, treeInfo)
	
	treeInfo.diameter = max(leftHeight+rightHeight, treeInfo.diameter)
	
	return max(leftHeight,rightHeight)+1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.right = BinaryTree(2)
        expected = 6
        actual = binaryTreeDiameter(root)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()