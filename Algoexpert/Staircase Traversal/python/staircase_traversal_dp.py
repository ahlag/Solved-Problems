import unittest

# O(k * n) time | O(n) space - where n is the height of the staircase and k is
# the number ofallowed steps
def staircaseTraversal(height, maxSteps):
    
    dp = (height+1) * [0]
    
    # There's only 1 way to get to 0 nd 1
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, height+1):
        for step in range(1, maxSteps+1):
            dp[i] += dp[i-step]
        # step = 1
        # while step <= maxSteps and (i-step) >= 0:
        #     dp[i] += dp[i-step]
        #     step += 1

    return dp[height]

def staircaseTraversal_while(height, maxSteps):
    
    waysToTop = [0 for _ in range(height + 1)]
    waysToTop[0] = 1
    waysToTop[1] = 1
    
    for currentHeight in range(2, height + 1):
        step = 1
        while step <= maxSteps and step <= currentHeight:
            waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
            step += 1

    return waysToTop[height]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)
        
    def test_case_2(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal_while(stairs, maxSteps)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()