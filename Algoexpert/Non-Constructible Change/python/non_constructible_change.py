import unittest

# O(nlogn) time | O(1) space
def nonConstructibleChange(coins):

    coins.sort()

    current_change_created = 0

    for coin in coins:
        if coin > current_change_created + 1:
            return current_change_created + 1 

        current_change_created += coin

    return current_change_created + 1

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = nonConstructibleChange(input)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()
