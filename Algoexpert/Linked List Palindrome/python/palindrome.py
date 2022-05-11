import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def linkedListPalindromeStraightforward(head):

    fast = head
    slow = head
    
    # Get the middle node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    # reverse node
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp
        
    # check palindrome
    left, right = head, prev
    while left and right:
        
        if left.value != right.value:
            return False
        
        left = left.next
        right = right.next
        
    return True

# O(n) time | O(1) space
def linkedListPalindromeReverse(head):
	slowNode = head
	fastNode = head
	
	while fastNode is not None and fastNode.next is not None:
		slowNode = slowNode.next
		fastNode = fastNode.next.next
	
	reversedSecondHalfNode = reverseLinkedList(slowNode)
	firstHalfNode = head
	
	while reversedSecondHalfNode is not None:
		if reversedSecondHalfNode.value != firstHalfNode.value:
			return False
		reversedSecondHalfNode = reversedSecondHalfNode.next
		firstHalfNode = firstHalfNode.next
	
	return True

def reverseLinkedList(head):
	previousNode, currentNode = None, head
	while currentNode is not None:
		nextNode = currentNode.next
		currentNode.next = previousNode
		previousNode = currentNode
		currentNode = nextNode
	return previousNode


# O(n) time | O(n) space
def linkedListPalindromeRecursive(head):
    isPalindromeResults = isPalindrome(head, head)
    return isPalindromeResults.outerNodesAreEqual

def isPalindrome(leftNode, rightNode):
	if rightNode is None:
		return LinkedListInfo(True, leftNode)
	
	recursiveCallResults = isPalindrome(leftNode, rightNode.next)
	leftNodeToCompare = recursiveCallResults.leftNodeToCompare
	outerNodesAreEqual = recursiveCallResults.outerNodesAreEqual
	
	recursiveIsEqual = outerNodesAreEqual and leftNodeToCompare.value == rightNode.value
	nextLeftNodeToCompare = leftNodeToCompare.next
	
	return LinkedListInfo(recursiveIsEqual, nextLeftNodeToCompare)

class LinkedListInfo:
	def __init__(self, outerNodesAreEqual, leftNodeToCompare):
		self.outerNodesAreEqual = outerNodesAreEqual
		self.leftNodeToCompare = leftNodeToCompare

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(2)
        head.next.next.next.next = LinkedList(1)
        head.next.next.next.next.next = LinkedList(0)
        expected = True
        actual = linkedListPalindromeStraightforward(head)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(2)
        head.next.next.next.next = LinkedList(1)
        head.next.next.next.next.next = LinkedList(0)
        expected = True
        actual = linkedListPalindromeRecursive(head)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(2)
        head.next.next.next.next = LinkedList(1)
        head.next.next.next.next.next = LinkedList(0)
        expected = True
        actual = linkedListPalindromeReverse(head)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
