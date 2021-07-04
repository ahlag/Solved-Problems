# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums_iterative(root):
    # Write your code here.
    stack = [(root, root.value)]
    branch_sums = []
	
    while stack:
		
        node, running_sum = stack.pop()

        if node.left is None and node.right is None:
            branch_sums.append(running_sum)
            continue
			
        if node.left:
            new_sum = node.left.value + running_sum
            stack.append((node.left, new_sum))
			
        if node.right:
            new_sum = node.right.value + running_sum
            stack.append((node.right, new_sum))
			
    return branch_sums[::-1]

def branchSums_recursive(root):
	branch_sums = []
    # return branchSums_reccursive_helper(root, 0, branch_sums)
	branchSums_reccursive_helper(root, 0, branch_sums)
	return branch_sums

# In reccusrive call we need to pass the current_ sum and the sum_list down the tree.
def branchSums_reccursive_helper(node, running_sum, branch_sums):
	
	running_sum += node.value
    # On reaching a leaf node. Append the sum to the sum list
	if node.left == None and node.right== None:
		branch_sums.append(running_sum)
		return

	if node.left:
		branchSums_reccursive_helper(node.left, running_sum, branch_sums)
		
	if node.right:
		branchSums_reccursive_helper(node.right, running_sum, branch_sums)

def main():
    
    BT = BinaryTree(1)
    BT.left = BinaryTree(2)
    BT.left.left = BinaryTree(4)
    BT.left.right = BinaryTree(5)
    BT.left.right.left = BinaryTree(10)
    BT.left.left.left = BinaryTree(8)
    BT.left.left.right = BinaryTree(9)
    BT.right = BinaryTree(3)
    BT.right.left = BinaryTree(6)
    BT.right.right = BinaryTree(7)
    
    print(branchSums_iterative(BT))
    print(branchSums_recursive(BT))
    
if __name__ == "__main__":
    main()
