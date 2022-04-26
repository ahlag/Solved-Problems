import unittest

# Time O(n) | Space O(1)
def findLoop(head):
    
	slow = head
	fast = head
	
	while fast and fast.next:
		
		slow = slow.next
		fast = fast.next.next
		
		if slow == fast:
			break
			
	cur = head
	
	while slow.next:
		
		if slow == cur:
			return slow
		
		slow = slow.next
		cur = cur.next

def findLoopAlgoAbridged(head):
    
    first = head.next
    second = head.next.next
    
    while first != second:
        first = first.next
        second = second.next.next
        
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first

class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

linkedListClass = StartLinkedList

class LinkedList(linkedListClass):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNthNode(self, n):
        counter = 1
        current = self
        while counter < n:
            current = current.next
            counter += 1
        return current


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.getNthNode(10).next = test.getNthNode(5)
        self.assertEqual(findLoop(test), test.getNthNode(5))
        self.assertEqual(findLoopAlgoAbridged(test), test.getNthNode(5))

if __name__ == "__main__":
    unittest.main()