import unittest

# Best: O(nlog(n)) time | O(log(n)) space
# Average: O(nlog(n)) time | O(log(n)) space
# Worst: O(n^2) time | O(log(n)) space
def quickSort(array):
    quickSortHelper(array, 0, len(array)-1)
    return array

def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[rightIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(pivotIdx, rightIdx, array)
    leftSubArrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubArrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)
        
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(quickSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

if __name__ == "__main__":
    unittest.main()