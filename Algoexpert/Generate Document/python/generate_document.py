import unittest

# O(n + m) time | O(c) space - where n is the number of characters, m is
# the length of the document, and c is the number of unique characters in 
# the characters string
def generateDocument(characters, document):

    character_counts = {}

    for character in characters:
        if character not in character_counts:
            character_counts[character] = 0
        character_counts[character] += 1

    for character in document:
        if character not in character_counts or character_counts[character] == 0:
            return False

        character_counts[character] -= 1

    return True

# O( m * (n + m)) time | O(1) space - where n is the number
# of characters and m is the length of document
def generateDocumentBrute(characters, document):
    for character in document:
        documentFrequency = countCharacterFrequency(character, document)
        characterFrequency = countCharacterFrequency(character, characters)
        if documentFrequency > characterFrequency:
            return False

    return True

def countCharacterFrequency(character, target):
	frequency = 0
	for char in target:
		if char == character:
			frequency += 1
			
	return frequency

# O( c * (n + m)) time | O(c) space - where n is the number
# of characters and m is the length of document
def generateDocumentSet(characters, document):

    alreadyCounted = set()

    for character in document:

        if character in alreadyCounted:
            continue

        documentFrequency = countCharacterFrequency(character, document)
        characterFrequency = countCharacterFrequency(character, characters)
        if documentFrequency > characterFrequency:
            return False

        alreadyCounted.add(character)

    return True

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        characters = "Bste!hetsi ogEAxpelrt x "
        document = "AlgoExpert is the Best!"
        expected = True
        actual = generateDocument(characters, document)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        characters = "Bste!hetsi ogEAxpelrt x "
        document = "AlgoExpert is the Best!"
        expected = True
        actual = generateDocumentBrute(characters, document)
        self.assertEqual(actual, expected)
        
    def test_case_3(self):
        characters = "Bste!hetsi ogEAxpelrt x "
        document = "AlgoExpert is the Best!"
        expected = True
        actual = generateDocumentSet(characters, document)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()