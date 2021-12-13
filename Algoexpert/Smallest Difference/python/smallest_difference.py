import unittest

# O(n^2) time | O(1) space - where n is the length of the array
def smallestDifferenceBrute(arrayOne, arrayTwo):

    smallest_difference = float('inf')
    resOne, resTwo = 0, 0

    for intOne in arrayOne:
        for intTwo in arrayTwo:
            difference = abs(intOne - intTwo)
            if difference < smallest_difference:
                smallest_difference = difference
                resOne = intOne
                resTwo = intTwo

    return [resOne, resTwo]

# O(nlog(n) + nloh(n)) time | O(1) space - where n is the length of the array
def smallestDifference(arrayOne, arrayTwo):

	arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float('inf')
	current  = float('inf')
	smallest_pair = []
	
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idxTwo += 1
		else:
			return [firstNum, secondNum]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	
	return smallestPair

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallestDifferenceBrute([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])

    def test_case_2(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])

if __name__ == "__main__":
    unittest.main()
