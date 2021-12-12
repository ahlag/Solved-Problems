import unittest

# O(n^2) time | O(1) space
def countInversionsBruteForce(array):

	inversions = 0
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i] > array[j]:
				inversions += 1

	return inversions

# O(nlogn) time | O(n) space - where n is the length of array
def countInversions(array):

    return countSubArrayInversions(array, 0, len(array))

def countSubArrayInversions(array, start, end):
	if end - start <= 1:
		return 0
	
	middle = start + (end - start) // 2
	left_inversions = countSubArrayInversions(array, start, middle)
	right_inversions = countSubArrayInversions(array, middle, end)
	merged_array_inversions = mergeSortAndCountInversions(array, start, middle, end)
	return left_inversions + right_inversions + merged_array_inversions

def mergeSortAndCountInversions(array, start, middle, end):
	sortedArray = []
	left = start
	right = middle
	inversions = 0
	
	while left < middle and right < end:
		if array[left] <= array[right]:
			sortedArray.append(array[left])
			left += 1
		else:
			inversions += middle - left
			sortedArray.append(array[right])
			right += 1
			
	sortedArray += array[left:middle] + array[right:end]
	for idx, num in enumerate(sortedArray):
		array[start + idx] = num
		
	return inversions

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 3, 3, 1, 9, 5, 6]
        expected = 5
        actual = countInversionsBruteForce(input)
        self.assertEqual(actual, expected)
        
    def test_case_2(self):
        input = [2, 3, 3, 1, 9, 5, 6]
        expected = 5
        actual = countInversions(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()