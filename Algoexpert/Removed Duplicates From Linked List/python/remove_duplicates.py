import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    
	head = linkedList
	
	while head.next is not None:
		
		if head.next.value == head.value:
			head.next = head.next.next
		else:
			head = head.next
		
	return linkedList

def removeDuplicatesFromLinkedList_two_while_loops(linkedList):
    
    current_node = linkedList

    while current_node is not None:

        next_distinct_node = current_node.next

        while next_distinct_node is not None and next_distinct_node.value == current_node.value:
            next_distinct_node = next_distinct_node.next

        current_node.next = next_distinct_node
        current_node = next_distinct_node

    return linkedList

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
    
testable_functions = [removeDuplicatesFromLinkedList, removeDuplicatesFromLinkedList_two_while_loops]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = LinkedList(1).addMany([3, 4, 5, 6])
        
        for f in testable_functions:
            actual = f(test)
            self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())
        
if __name__ == "__main__":
    unittest.main()