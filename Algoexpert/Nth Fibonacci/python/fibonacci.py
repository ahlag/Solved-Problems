import unittest

# O(2^n) time | O(n) space
def fibonacci_recursive(n):

    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# O(n) time | O(n) space
def fibonacci_memo(n, memoize={1: 0, 2: 1}):

    if n in memoize:
        return memoize[n]   
    else:
        memoize[n] = fibonacci_memo(n-1, memoize) + fibonacci_memo(n-2, memoize)
        return memoize[n]
    
# O(n) time | O(1) space
def fibonacci_array(n):

    last_two = [0, 1]

    for i in range(3, n+1):
        nextFib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = nextFib
		
    return last_two[1] if n > 1 else last_two[0]

## O(n) time | O(1) space
def fibonacci_variable(n):

    ## second, first
    ## [0, 1]
    first, second = 1, 0

    for i in range(3, n+1):
        nextFib = first + second
        second = first
        first = nextFib
		
    return first if n > 1 else second

testable_functions = [
                        fibonacci_recursive, 
                        fibonacci_memo,
                        fibonacci_array,
                        fibonacci_variable
                    ]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        
        for f in testable_functions:
            actual = f(6)
            self.assertEqual(actual, 5)

if __name__ == "__main__":
    unittest.main()