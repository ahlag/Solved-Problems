## This problem is known as Sum of subtree depths for every node of a given Binary Tree
## https://www.geeksforgeeks.org/sum-of-subtree-depths-for-every-node-of-a-given-binary-tree/
import unittest

def nodeDepths_recursive(root):
    return nodeDepths_recursiveHelper(root, 0)
	
def nodeDepths_recursiveHelper(root, depth):
	
	if root is None:
		return 0

	return depth + nodeDepths_recursiveHelper(root.left, depth+1) + nodeDepths_recursiveHelper(root.right, depth+1)

def nodeDepths_iterative(root):

    sum_of_depths, depth = 0, 0
    stack = [(root, depth)]

    while stack:

        node, depth = stack.pop()
		
        sum_of_depths += depth

        if node.left:
            stack.append((node.left, depth+1))
			
        if node.right:
            stack.append((node.right, depth+1))

    return sum_of_depths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

testable_functions = [nodeDepths_recursive, nodeDepths_iterative]

class TestProgram(unittest.TestCase):
    def test_case(self):
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