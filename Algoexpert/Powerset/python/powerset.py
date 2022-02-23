import unittest

def powersetBitManipulation(array):

    n = len(array)
    no_of_combinations = 2**n

    combinations = []
    for i in range(no_of_combinations):
        subarray = []
        for k in range(n):
            if i & (1 << k):
                subarray.append(array[k])
        combinations.append(subarray)

    return combinations	

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = list(map(lambda x: set(x), powersetBitManipulation([1, 2, 3])))
        self.assertTrue(len(output) == 8)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)
        self.assertTrue(set([3]) in output)
        self.assertTrue(set([1, 3]) in output)
        self.assertTrue(set([2, 3]) in output)
        self.assertTrue(set([1, 2, 3]) in output)

if __name__ == "__main__":
    unittest.main()