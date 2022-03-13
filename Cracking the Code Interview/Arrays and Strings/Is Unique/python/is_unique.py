import unittest
from collections import defaultdict
import time

def is_unique_chars_pythonic(string):
    
    return len(string) == len(set(string))

def is_unique_chars_algorithmic(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False
    
    # this is a pythonic and faster way to initialize an array with a fixed value.
    #  careful though it won't work for a doubly nested array
    char_set = [False] * 128
    
    for i in range(len(string)):
        ascii = ord(string[i]) - 97
        if char_set [ascii] is False:
            char_set [ascii] = True
        else:
            return False

    return True

def is_unique_chars_using_set(string: str) -> bool:
    charset = set()
    
    for char in string:
        if char in charset:
            return False
        charset.add(char)

    return True

# O(NlogN)
def is_unique_chars_sorting(string: str) -> bool:
    
    string = sorted(string)
    
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
        
    return True

def is_unique_chars_using_dictionary(string: str) -> bool:
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True

def is_unique_bit_vector(string):
    """Uses bitwise operation instead of extra data structures."""
    # Assuming character set is ASCII (128 characters)
    
    if len(string) > 128:
        return False
    
    checker = 0
    for char in string:
        val = ord(char)
        if checker & (1 << val):
            return False
        checker |= (1 << val)
        
    return True

class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_chars_pythonic,
        is_unique_chars_algorithmic,
        is_unique_bit_vector,
        is_unique_chars_using_dictionary,
        is_unique_chars_using_set,
        is_unique_chars_sorting,
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()