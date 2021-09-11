import unittest

# O(nlog(n)) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)

    if fastest:
        total_speed = sum([ max(speed1, speed2) \
                        for speed1, speed2 in zip(redShirtSpeeds, blueShirtSpeeds)])
    else:
        total_speed = sum([ max(speed1, speed2) \
                        for speed1, speed2 in zip(redShirtSpeeds, blueShirtSpeeds)])


    return total_speed

def tandemBicycle_algoexpert(redShirtSpeeds, blueShirtSpeeds, fastest):

    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)

    total_speed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
        total_speed += max(rider1, rider2)

    return total_speed

def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        redShirtSpeeds = [5, 5, 3, 9, 2]
        blueShirtSpeeds = [3, 6, 7, 2, 1]
        fastest = True
        expected = 32
        actual = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
        self.assertEqual(actual, expected)
        
    def test_case_2(self):
        redShirtSpeeds = [5, 5, 3, 9, 2]
        blueShirtSpeeds = [3, 6, 7, 2, 1]
        fastest = False
        expected = 25
        actual = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()