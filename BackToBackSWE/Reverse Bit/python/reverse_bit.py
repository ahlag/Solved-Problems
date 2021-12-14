import unittest

def reverseBits(input):
    '''
    :type input: int
    :rtype: int
    '''
    output = 0
    while input:
        output = output << 1
        if input & 1 == 1:
            output |= 1
        
        input = input >> 1
    return output

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        inputs = [1, 10, 9090]
        expected_outputs = [1, 5, 4209]
        
        for (input, expected_output) in zip(inputs, expected_outputs):
            actual = reverseBits(input)
            self.assertEqual(actual, expected_output)

if __name__ == "__main__":
    unittest.main()