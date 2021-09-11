import unittest

# O(n^2) time | O(1) space
def threeNumberSum(array, targetSum):

    array.sort()

    results = []

    n = len(array)

    for cur in range(0, n-2):

        left, right = cur + 1, n - 1

        while left < right:
            
            if targetSum == (array[cur] + array[left] + array[right]):
                results.append([array[cur], array[left], array[right]])

            if array[right] + array[left] > targetSum - array[cur]:
                right -= 1
            else:
                left += 1

    return results

def threeNumberSum_algoexpert(array, target_sum):

    array.sort()
    triplets = []

    n = len(array)

    for cur in range(0, n-2):

        left, right = cur + 1, n - 1

        while left < right:
            current_sum = array[cur] + array[left] + array[right]
            
            if current_sum == target_sum:
                triplets.append([array[cur], array[left], array[right]])
                left += 1
                right -= 1

            elif current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1

    return triplets

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
        
    def test_case_2(self):
        self.assertEqual(threeNumberSum_algoexpert([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])

if __name__ == "__main__":
    unittest.main()