import unittest

# O(n^2) time | O(1) space - where n is the length of the iput string
def firstNonRepeatingCharacter(string):

    for i in range(len(string)):

        found_duplicate = False
        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                found_duplicate = True

        if not found_duplicate:
            return i

    return -1

# O(n) time | O(1) space - where n is the length of the iput string
def firstNonRepeatingCharacterLinear(string):
    character_frequencies = {}

    for character in string:
        character_frequencies[character] = character_frequencies.get(character, 0) + 1

    for i in range(len(string)):
        character = string[i]
        if character_frequencies[character] == 1:
            return i
    return -1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "abcdcaf"
        expected = 1
        actual = firstNonRepeatingCharacter(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = "abcdcaf"
        expected = 1
        actual = firstNonRepeatingCharacterLinear(input)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()