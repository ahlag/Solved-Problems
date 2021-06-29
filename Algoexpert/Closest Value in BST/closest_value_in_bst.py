def findClosestValueInBst_recursive(tree, target):
    
    def traverse(tree, target, closest):

        if tree is None:
            return closest
    
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value

        if target < tree.value:
            return traverse(tree.left, target, closest)
        elif target > tree.value:
            return traverse(tree.right, target, closest)
        else:
            return closest
	
    return traverse(tree, target, tree.value)

def findClosestValueInBst_iterative(tree, target):
    
	def traverse(tree, target, closest):

		curr = tree
		
		while curr is not None:
			
			if abs(target - closest) > abs(target - curr.value):
				closest = curr.value
				
			if target < curr.value:
				curr = curr.left
			elif target > curr.value:
				curr = curr.right
			else:
				break
				
		return closest
	
	return traverse(tree, target, tree.value)

class BST:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def main():
    
    bst = BST(10)
    bst.left = BST(5)
    bst.left.left = BST(2)
    bst.left.right = BST(5)
    bst.left.left.left = BST(1)
    bst.right = BST(15)
    bst.right.left = BST(13)
    bst.right.right = BST(22)
    bst.right.left.right = BST(14)
    
    print(findClosestValueInBst_recursive(bst, 12))
    print(findClosestValueInBst_iterative(bst, 12))
    
if __name__ == "__main__":
    main()
