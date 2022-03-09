import unittest

# time O(n) | space O(d)
def validateBstRecursion(tree):
	return validateBstHelper(tree, float('-inf'), float('inf'))
    
def validateBstHelper(tree, minValue, maxValue):
	
	if tree is None:
		return True
	
	if tree.value < minValue or tree.value >= maxValue:
		return False
	
	leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
	
	return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)

# time O(n) | space O(1)
def validateBstIterative(tree):

	if not tree:
		return True
    
	min_value = -float('inf')
	max_value = float('inf')
	
	stack = [(tree, min_value, max_value)]
	
	while stack:
		
		node, min_value, max_value = stack.pop()
		
		if node.value < min_value or node.value >= max_value:
			return False
			
		if node.left:
			stack.append((node.left, min_value, node.value))
			
		if node.right:
			stack.append((node.right, node.value, max_value))
	
	return True

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
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        self.assertEqual(validateBstRecursion(root), True)
        
    def test_case_2(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        self.assertEqual(validateBstIterative(root), True)

if __name__ == "__main__":
    unittest.main()