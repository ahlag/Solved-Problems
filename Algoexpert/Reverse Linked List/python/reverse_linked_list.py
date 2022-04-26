import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedListRecursive(head):
	
	if head is None or head.next is None:
		return head
	
	p = reverseLinkedListRecursive(head.next)
	head.next.next = head
	head.next = None
	
	return p

def reverseLinkedListIterative(head):

    previousNode, currentNode = None, head

    while currentNode:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode

    return previousNode

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
        test = LinkedList(0).addMany([1, 2, 3, 4, 5])
        result = reverseLinkedListRecursive(test).getNodesInArray()
        expected = LinkedList(5).addMany([4, 3, 2, 1, 0]).getNodesInArray()
        self.assertEqual(result, expected)
        
    def test_case_2(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5])
        result = reverseLinkedListIterative(test).getNodesInArray()
        expected = LinkedList(5).addMany([4, 3, 2, 1, 0]).getNodesInArray()
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()