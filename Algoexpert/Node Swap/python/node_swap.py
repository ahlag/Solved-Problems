import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(n) space
def nodeSwapRecursive(head):
    
    if head is None or head.next is None:
        return head
    
    nextNode = head.next
    head.next = nodeSwapRecursive(head.next.next)
    nextNode.next = head

    return nextNode

# O(n) time | O(1) space
def nodeSwapIterative(head):
    
	dummy = LinkedList(-1)
	dummy.next = head
	prevNode = dummy
	
	while prevNode.next is not None and prevNode.next.next is not None:
		firstNode = prevNode.next
		secondNode = prevNode.next.next
		
		# prevNode -> firstNode -> secondNode
		
		firstNode.next = secondNode.next
		secondNode.next = firstNode
		prevNode.next = secondNode
		# prevNode -> secondNode -> firstNode
		
		prevNode = firstNode
		
	return dummy.next

class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = LinkedList(0).addMany([1, 2, 3, 4, 5])
        expectedNodes = [1, 0, 3, 2, 5, 4]
        output = nodeSwapRecursive(linkedList)
        self.assertEqual(output.getNodesInArray(), expectedNodes)
    
    def test_case_2(self):
        linkedList = LinkedList(0).addMany([1, 2, 3, 4, 5])
        expectedNodes = [1, 0, 3, 2, 5, 4]
        output = nodeSwapIterative(linkedList)
        self.assertEqual(output.getNodesInArray(), expectedNodes)

if __name__ == "__main__":
    unittest.main()
