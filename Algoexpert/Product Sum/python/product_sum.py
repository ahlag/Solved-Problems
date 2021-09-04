import unittest

def productSum(array):
    
	def helper(array, depth):
		
		total = 0
		for element in array:
			
			if type(element) is list:
				total += helper(element, depth+1)
			else:
				total += element
			
		return total * depth
	
	return helper(array, 1)

def productSum_ref(array, multiplier=1):
		
	total = 0
	for element in array:
		if type(element) is list:
			total += productSum_ref(element, multiplier+1)
		else:
			total += element

	return multiplier * total

testable_functions = [productSum, productSum_ref]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        # self.assertEqual(productSum(test), 12)
        
        for f in testable_functions:
            actual = f(test)
            self.assertEqual(actual, 12)

if __name__ == "__main__":
    unittest.main()