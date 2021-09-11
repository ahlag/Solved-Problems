from string import ascii_lowercase
import unittest

def caesarCipherEncryptor(string, key):

    key = key % 26

    caesar_table = { char: chr((idx + key) % 26 + 97) \
                        for char, idx in zip(ascii_lowercase, range(0,26)) }

    caesar_cipher = ''
    for char in string:
        caesar_cipher += caesar_table[char]

    return caesar_cipher

def caesarCipherEncryptor_algoexpert(string, key):

    new_letters = []
    
    new_key = key % 26
    
    for letter in string:
        new_letters.append(getNewLetter(letter, new_key))
        
    return "".join(new_letters)

def getNewLetter(letter, key):
    
    new_letter_code = ord(letter) + key
    
    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 2), "zab")
        
if __name__ == "__main__":
    unittest.main()