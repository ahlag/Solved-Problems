import unittest

# O(n) time | O(1) space
def longestPeak(array):
    
    queries.sort()

    time_taken = 0
    for i, duration in enumerate(queries):
        queries_left = len(queries) - (i + 1)
        time_taken += duration * queries_left

    return time_taken

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longestPeak(array), expected)
    
if __name__ == "__main__":
    main()