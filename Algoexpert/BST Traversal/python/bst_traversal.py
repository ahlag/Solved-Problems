def inOrderTraverse(tree, array):
    # Write your code here.
	if tree is not None:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array

def preOrderTraverse(tree, array):
    # Write your code here.
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array


def postOrderTraverse(tree, array):
    # Write your code here.
	if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array

import unittest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)

        inOrder = [1, 2, 5, 5, 10, 15, 22]
        preOrder = [10, 5, 2, 1, 5, 15, 22]
        postOrder = [1, 2, 5, 5, 22, 15, 10]

        self.assertEqual(inOrderTraverse(root, []), inOrder)
        self.assertEqual(preOrderTraverse(root, []), preOrder)
        self.assertEqual(postOrderTraverse(root, []), postOrder)
        
if __name__ == "__main__":
    unittest.main()

