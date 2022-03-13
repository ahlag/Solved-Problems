import unittest

def urlify_algo(s, length):
    # convert to list because Python strings are immutable
    charList = list(s)
    newIndex = len(charList)

    for i in reversed(range(length)):
        if charList[i] == " ":
            charList[newIndex-3: newIndex] = "%20"
            newIndex -= 3
        else:
            charList[newIndex-1] = charList[i]
            newIndex -= 1

    return "".join(charList[newIndex:])
    
def urlify_pythonic(s, length):
    """solution using standard library"""
    return s[:length].replace(" ", "%20")

class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    testable_functions = [
                            urlify_algo, 
                            # urlify_pythonic
                        ]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = urlify(*args)
                assert actual == expected, f"Failed {urlify.__name__} for: {[*args]}"


if __name__ == "__main__":
    unittest.main()