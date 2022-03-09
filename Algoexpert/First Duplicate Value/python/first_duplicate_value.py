import unittest

# time O(n^2) | space O(1)
def firstDuplicateValueBruteForce(array):

    minimumSecondIndex = len(array)
    for i in range(len(array)):
        value = array[i]
        for j in range(i+1, len(array)):
            valueToCompare = array[j]
            if value == valueToCompare:
                minimumSecondIndex = min(minimumSecondIndex, j)

    if minimumSecondIndex == len(array):
        return -1

    return array[minimumSecondIndex]

# time O(n) | space O(n)
def firstDuplicateValueHashSet(array):

    found = set()
    for i in range(len(array)):
        if array[i] in found:
            return array[i]
        found.add(array[i])

    return -1

def firstDuplicateValueOptimal(array):

    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = firstDuplicateValueHashSet(input)
        self.assertEqual(actual, expected)
        
    def test_case_2(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = firstDuplicateValueBruteForce(input)
        self.assertEqual(actual, expected)
        
    def test_case_3(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = firstDuplicateValueOptimal(input)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()