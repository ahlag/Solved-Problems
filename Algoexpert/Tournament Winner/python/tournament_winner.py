import unittest

def tournamentWinner_naive(competitions, results):

    teams = {}
    for competition, result in zip(competitions, results):

        if competition[0] not in teams:
            teams[competition[0]] = 0

        if competition[1] not in teams:
            teams[competition[1]] = 0

        if result == 0:
            teams[competition[1]] += 1

        if result == 1:
            teams[competition[0]] += 1

    return max(teams, key=teams.get)

def tournamentWinner_optimized(competitions, results):

    best_team = ""
    scores = {best_team: 0}

    for i, competition in enumerate(competitions):
        result = results[i]
        home_team, away_team = competition

        winning_team = home_team if result == 1 else away_team

        update_scores(winning_team, 3, scores)

        if scores[winning_team] > scores[best_team]:	
            best_team = winning_team

    return best_team

def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournamentWinner_naive(competitions, results)
        self.assertEqual(actual, expected)
        
    def test_case_2(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournamentWinner_optimized(competitions, results)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()