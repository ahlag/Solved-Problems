## This problem is known as Sum of subtree depths for every node of a given Binary Tree
## https://www.geeksforgeeks.org/sum-of-subtree-depths-for-every-node-of-a-given-binary-tree/
import unittest

def nodeDepths_recursive(root):
    return nodeDepths_recursiveHelper(root, 0)
	
def nodeDepths_recursiveHelper(root, depth):
	
	if root is None:
		return 0

	return depth + nodeDepths_recursiveHelper(root.left, depth+1) + nodeDepths_recursiveHelper(root.right, depth+1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

testable_functions = [nodeDepths_recursive]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        
        for f in testable_functions:
            actual = f(root)
            self.assertEqual(actual, 16)
        
if __name__ == "__main__":
    unittest.main()