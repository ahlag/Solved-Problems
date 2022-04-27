import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array

def shiftLinkedList(head, k):
	
	listTail = head
	length = 1
	while listTail.next:
		listTail = listTail.next
		length += 1
	
	offset = abs(k) % length
	if offset == 0:
		return head
	
	newTailPosition = length - offset if k > 0 else offset
	
	newTail = head
	for _ in range(1, newTailPosition):
		newTail = newTail.next
	
	newHead = newTail.next
	newTail.next = None
	listTail.next = head
	
	return newHead

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(3)
        head.next.next.next.next = LinkedList(4)
        head.next.next.next.next.next = LinkedList(5)
        result = shiftLinkedList(head, 2)
        array = linkedListToArray(result)

        expected = [4, 5, 0, 1, 2, 3]
        self.assertEqual(expected, array)

if __name__ == "__main__":
    unittest.main()