import unittest

# Time O(n^2) | Space O(n)
def arrayOfProductsBruteForce(array):

    n = len(array)
    output = [1] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                output[i] = array[j] * output[i]

    return output

def arrayOfProductsExtraArrays(array):

    products = [1 for _ in range(len(array))]
    left_products = [1 for _ in range(len(array))]
    right_products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        left_products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        right_products[i] = right_running_product
        right_running_product *= array[i]

    for i in range(len(array)):
        products[i] = left_products[i] * right_products[i]

    return products

def arrayOfProductsOptimized(array):
    products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running_product
        right_running_product *= array[i]

    return products
    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = arrayOfProductsOptimized(array)
        self.assertEqual(actual, expected)

        
if __name__ == "__main__":
    unittest.main()