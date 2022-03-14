import unittest

# O(n) time | O(1) space
def longestPeak(array):
    
	longestPeakLength = 0
	i = 1
	n = len(array)
	while i < n-1:
		isPeak = array[i-1] < array[i] and array[i] > array[i+1]
		if not isPeak:
			i += 1
			continue
			
		leftIdx = i - 2
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
			leftIdx -= 1
		rightIdx = i + 2
		while rightIdx < n and array[rightIdx] < array[rightIdx - 1]:
			rightIdx += 1
		
		currentPeakLength = rightIdx - leftIdx - 1
		longestPeakLength = max(longestPeakLength, currentPeakLength)
		i = rightIdx

	return longestPeakLength

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longestPeak(array), expected)
    
if __name__ == "__main__":
    unittest.main()