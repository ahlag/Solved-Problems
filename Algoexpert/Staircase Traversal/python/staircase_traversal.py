import unittest

# O(k^n) time | O(n) space
def staircaseTraversal(height, maxSteps):
    
    if height <= 1:
        return 1
    
    numberOfWays = 0
    
    for step in range(1, min(maxSteps, height) + 1):
        numberOfWays += staircaseTraversal(height - step, maxSteps)

    return numberOfWays

class TestProgram(unittest.TestCase):
    def test_case(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()