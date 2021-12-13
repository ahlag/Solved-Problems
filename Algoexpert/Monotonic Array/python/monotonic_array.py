import unittest

# O(n) time | O(1) space - where n is the length of the array
def isMonotonicBool(array):
    
	is_non_decreasing = True
	is_non_increasing = True
	
	for i in range(1, len(array)):
		if array[i] - array[i-1] > 0:
			is_non_decreasing = False
		elif array[i] - array[i-1] < 0:
			is_non_increasing = False
			
	return is_non_decreasing or is_non_increasing

# O(n) time | O(1) space - where n is the length of the array
def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction == array[i] - array[i-1]
            continue
        if breaksDirection(direction, array[i-1], array[i]):
            return False

    return True

def breaksDirection(direction, previousInt, currentInt):
	difference = currentInt - previousInt
	if direction > 0:
		return difference < 0
	return difference > 0

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonicBool(array)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
