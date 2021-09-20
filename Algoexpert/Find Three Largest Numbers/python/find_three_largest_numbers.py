import unittest

# O(n) time | O(1) space
def findThreeLargestNumbers_personal(array):

    results = [ -float('inf') ] * 3
    n = len(array)

    for i in range(n):

        if array[i] > results[0]:

            results[0] = array[i]

            for j in range(2):

                if results[j] > results[j+1]:
                    results[j], results[j+1] = results[j+1], results[j]

    return results

# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)
    return three_largest

def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)
    
def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])

    def test_case_2(self):
        self.assertEqual(findThreeLargestNumbers_personal([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])

if __name__ == "__main__":
    unittest.main()