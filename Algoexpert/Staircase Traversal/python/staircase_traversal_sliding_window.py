import unittest

# O(n) time | O(n) space - where n is the height of the staircase
def staircaseTraversal(height, maxSteps):
    
    waysToTop = [1]
    currentNumberOfWays = 0
    
    for currentHeight in range(1, height+1):
        startOfWindow = currentHeight - maxSteps - 1
        endOfWindow = currentHeight - 1
        if startOfWindow >= 0:
            currentNumberOfWays -= waysToTop[startOfWindow]
        
        currentNumberOfWays += waysToTop[endOfWindow]
        waysToTop.append(currentNumberOfWays)

    return waysToTop[height]

class TestProgram(unittest.TestCase):
    def test_case(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()