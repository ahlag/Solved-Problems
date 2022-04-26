import unittest

# Time O(n+m) | Space O(1)
def mergeLinkedLists(headOne, headTwo):
    
	sentinel = LinkedList(0)
	cur = sentinel
	
	while headOne and headTwo:
		
		if headOne.value > headTwo.value:
			cur.next = headTwo
			headTwo = headTwo.next
		elif headOne.value <= headTwo.value:
			cur.next = headOne
			headOne = headOne.next
		
		cur = cur.next
	
	if headOne is None:
		cur.next = headTwo
	elif headTwo is None:
		cur.next = headOne
		
	return sentinel.next

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

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
        list1 = LinkedList(2).addMany([6, 7, 8])
        list2 = LinkedList(1).addMany([3, 4, 5, 9, 10])
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

if __name__ == "__main__":
    unittest.main()
