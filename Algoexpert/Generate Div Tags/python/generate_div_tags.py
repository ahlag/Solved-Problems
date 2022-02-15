import unittest

# O((2n)!/((n!((n+1)!))) time | 0((2n)!/((n!((n+1)!)))) space -
# where n is the input number
def generateDivTags(numberOfTags):

    matchedDivTags = []
    generateDivTagsFromPrefix(numberOfTags, numberOfTags, "", matchedDivTags)

    return matchedDivTags

def generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded, prefix, result):
    
    if openingTagsNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsFromPrefix(openingTagsNeeded - 1, closingTagsNeeded, newPrefix, result)
        
    if openingTagsNeeded < closingTagsNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded - 1, newPrefix, result)
    
    if closingTagsNeeded == 0:
        result.append(prefix)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = 3
        expected = [
            "<div><div><div></div></div></div>",
            "<div><div></div><div></div></div>",
            "<div><div></div></div><div></div>",
            "<div></div><div><div></div></div>",
            "<div></div><div></div><div></div>",
        ]
        actual = generateDivTags(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()