import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    
	newLinkedListHeadPointer = LinkedList(0)
	currentNode = newLinkedListHeadPointer
	carry = 0
	
	nodeOne = linkedListOne
	nodeTwo = linkedListTwo
	
	while nodeOne or nodeTwo or carry != 0:
		
		valueOne = nodeOne.value if nodeOne is not None else 0
		valueTwo = nodeTwo.value if nodeTwo is not None else 0
		sumOfValues = valueOne + valueTwo + carry
		
		newValue = sumOfValues % 10
		newNode = LinkedList(newValue)
		currentNode.next = newNode
		currentNode = currentNode.next
		
		carry = sumOfValues // 10
		nodeOne = nodeOne.next if nodeOne is not None else None
		nodeTwo = nodeTwo.next if nodeTwo is not None else None
		
	return newLinkedListHeadPointer.next

class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = sumOfLinkedLists(ll1, ll2)
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))
        
if __name__ == "__main__":
    unittest.main()