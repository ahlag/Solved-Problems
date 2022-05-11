import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space
def zipLinkedList(linkedList):
    if linkedList.next is None or linkedList.next.next is None:
        return linkedList
    
    firstHalfHead = linkedList
    secondHalfHead = splitLinkedList(linkedList)
    
    reversedSecondHalfHead = reverseLinkedList(secondHalfHead)
    
    return interweaveLinkedLists(firstHalfHead, reversedSecondHalfHead)

def splitLinkedList(linkedList):
    slowIterator = linkedList
    fastIterator = linkedList
    while fastIterator is not None and fastIterator.next is not None:
        slowIterator = slowIterator.next
        fastIterator = fastIterator.next.next
        
    secondHalfHead = slowIterator.next
    slowIterator.next = None
    return secondHalfHead

def interweaveLinkedLists(linkedList1, linkedList2):
    linkedList1Iterator = linkedList1
    linkedList2Iterator = linkedList2
    while linkedList1Iterator is not None and linkedList2Iterator is not None:
        linkedList1IteratorNext = linkedList1Iterator.next
        linkedList2IteratorNext = linkedList2Iterator.next
        
        linkedList1Iterator.next = linkedList2Iterator
        linkedList2Iterator.next = linkedList1IteratorNext
        
        linkedList1Iterator = linkedList1IteratorNext
        linkedList2Iterator = linkedList2IteratorNext

    return linkedList1

def reverseLinkedList(linkedList):
    previousNode, currentNode = None, linkedList
    while currentNode is not None:
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
        head = LinkedList(1).addMany([2, 3, 4, 5, 6])
        expected = [1, 6, 2, 5, 3, 4]
        actual = zipLinkedList(head).getNodesInArray()
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()