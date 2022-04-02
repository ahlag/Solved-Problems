import time
import unittest

from isodate import duration_isoformat

def string_compression_sliding_window(string):
    
    n = len(string)
    compressed_string = []
    i = 0
    while i < n:
        
        j = i + 1
        while j < n and string[j] == string[i]:
            j += 1
            
        cnt = j - i
        
        compressed_string += string[i] + str(cnt)
        
        i = j
    
    return min(string, "".join(compressed_string), key=len)

def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  # noqa
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    if counter:
        compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, "".join(compressed), key=len)

class Test(unittest.TestCase):
    
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    
    testable_functions = [
        compress_string,
        string_compression_sliding_window
    ]
    
    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")

if __name__ == '__main__':
    unittest.main()
    