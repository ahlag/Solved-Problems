import unittest

# O(n^2) time | O(1) s@ace - where n is the number of cities
def validStartingCity(distances, fuel, mpg):

    numberOfCities = len(distances)

    for startCityIdx in range(numberOfCities):

        milesRemaining = 0

        for currentCityIdx in range(startCityIdx, startCityIdx + numberOfCities):

            if milesRemaining < 0:
                continue

            currentCityIdx = currentCityIdx % numberOfCities

            milesRemaining += (fuel[currentCityIdx] * mpg) - distances[currentCityIdx]

        if milesRemaining >= 0:
            return startCityIdx

    # This line should never be reached if the input is correct
    return -1

# O(n) time | O(1) space - where n is the number of cities
def validStartingCityOptimal(distances, fuel, mpg):
    numberOfCities = len(distances)
    milesRemaining = 0

    indexOfStartingCityCandidate = 0
    milesRemainingAtStartingCityCandidate = 0

    for cityIdx in range(1, numberOfCities):
        distanceFromPreviousCity = distances[cityIdx - 1]
        fuelFromPreviousCity = fuel[cityIdx - 1]
        milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity

        if milesRemaining < milesRemainingAtStartingCityCandidate:
            milesRemainingAtStartingCityCandidate = milesRemaining
            indexOfStartingCityCandidate = cityIdx

    return indexOfStartingCityCandidate

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        distances = [5, 25, 15, 10, 15]
        fuel = [1, 2, 1, 0, 3]
        mpg = 10
        expected = 4
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        distances = [5, 25, 15, 10, 15]
        fuel = [1, 2, 1, 0, 3]
        mpg = 10
        expected = 4
        actual = validStartingCityOptimal(distances, fuel, mpg)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()