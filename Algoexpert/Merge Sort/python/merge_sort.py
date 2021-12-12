import unittest

# Best: O(nlog(n)) time | O(nlog(n)) space
# Average: O(nlog(n)) time | O(nlog(n)) space
# Worst: O(nlog(n)) time | O(nlog(n)) space
def mergeSort(array):

    if len(array) == 1:
        return array
    middle_idx = len(array) // 2
    left_half = array[:middle_idx]
    right_half = array[middle_idx:]
    return mergeSortedArrays(mergeSort(left_half), mergeSort(right_half))

def mergeSortedArrays(left_half, right_half):

    sorted_array = [None] * (len(left_half) + len(right_half))

    k = i = j = 0

    while i < len(left_half) and j < len(right_half):

        if left_half[i] <= right_half[j]:
            sorted_array[k] = left_half[i]
            i += 1
        else:
            sorted_array[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        sorted_array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        sorted_array[k] = right_half[j]
        j += 1
        k += 1

    return sorted_array

# Best: O(nlog(n)) time | O(n) space
# Average: O(nlog(n)) time | O(n) space
# Worst: O(nlog(n)) time | O(n) space
def mergeSortOptimized(array):

    if len(array) <= 1:
        return array

    auxiliary_array = array[:]
    mergeSortHelper(array, 0, len(array)-1, auxiliary_array)
    return array

def mergeSortHelper(main_array, start_idx, end_idx, auxiliary_array):

    if start_idx == end_idx:
        return

    middle_idx = (start_idx + end_idx) // 2
    mergeSortHelper(auxiliary_array, start_idx, middle_idx, main_array)
    mergeSortHelper(auxiliary_array, middle_idx+1, end_idx, main_array)
    doMerge(main_array, start_idx, middle_idx, end_idx, auxiliary_array)

def doMerge(main_array, start_idx, middle_idx, end_idx, auxiliary_array):
    k = start_idx
    i = start_idx
    j = middle_idx + 1

    while i <= middle_idx and j <= end_idx:
        if auxiliary_array[i] <= auxiliary_array[j]:
            main_array[k] = auxiliary_array[i]
            i += 1
        else:
            main_array[k] = auxiliary_array[j]
            j += 1
        k += 1

    while i <= middle_idx:
        main_array[k] = auxiliary_array[i]
        i += 1
        k += 1

    while j <= end_idx:
        main_array[k] = auxiliary_array[j]
        j += 1
        k += 1

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(mergeSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
        
    def test_case_2(self):
        self.assertEqual(mergeSortOptimized([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
        
if __name__ == "__main__":
    unittest.main()