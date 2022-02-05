import unittest

# O(n) time | O(n) space - where n is the height of the staircase and k is
# the number ofallowed steps
def staircaseTraversal(height, maxSteps):

	return numberOfWaysToTop(height, maxSteps, {0: 1, 1: 1})

def numberOfWaysToTop(height, maxSteps, memo):

    if height in memo:
        return memo[height]

    numberOfWays = 0

    for step in range(1, min(height, maxSteps)+1):
        numberOfWays += numberOfWaysToTop(height - step, maxSteps, memo)
    
    memo[height] = numberOfWays

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