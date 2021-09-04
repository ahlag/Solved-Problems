import unittest

def classPhotos(redShirtHeights, blueShirtHeights):
	
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	if redShirtHeights[0] <  blueShirtHeights[0]:
		shirtColorInFirstRow = "RED"
	else:
		shirtColorInFirstRow = "BLUE"
		
	for i in range(len(redShirtHeights)):
		
		redShirtHeight = redShirtHeights[i]
		blueShirtHeight = blueShirtHeights[i]
		
		if shirtColorInFirstRow == "RED":
			if redShirtHeight >= blueShirtHeight:
				return False
		else:
			if redShirtHeight <= blueShirtHeight:
				return False
			
	return True

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        redShirtHeights = [5, 8, 1, 3, 4]
        blueShirtHeights = [6, 9, 2, 4, 5]
        expected = True
        actual = classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()
