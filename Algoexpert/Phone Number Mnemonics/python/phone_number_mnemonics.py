import unittest

# O(4^n * n) time | O(4^n * n) space - where n is the length of
# phone number
def phoneNumberMnemonics(phoneNumber):
    
	currentMnemonic = ["0"] * len(phoneNumber)
	mnemonicsFound = []
	print(currentMnemonic)
	phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonic, mnemonicsFound)
	
	return mnemonicsFound

def phoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonic, mnemonicsFound):
	
	if idx == len(phoneNumber):
		mnemonic = "".join(currentMnemonic)
		mnemonicsFound.append(mnemonic)
	else:
		digit = phoneNumber[idx]
		letters = DIGIT_LETTERS[digit]
		for letter in letters:
			currentMnemonic[idx] = letter
			phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currentMnemonic, mnemonicsFound)
	

DIGIT_LETTERS = {
	"0": ["0"],
	"1": ["1"],
	"2": ["a", "b", "c"],
	"3": ["d", "e", "f"],
	"4": ["g", "h", "i"],
	"5": ["j", "k", "l"],
	"6": ["m", "n", "o"],
	"7": ["p", "q", "r", "s"],
	"8": ["t", "u", "v"],
	"9": ["w", "x", "y", "z"],
}

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        phoneNumber = "1905"
        expected = ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"]
        actual = phoneNumberMnemonics(phoneNumber)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()