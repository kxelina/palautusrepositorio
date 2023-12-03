class TennisGame:
    SCORE = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def _get_equal_scores(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def _get_advantage_or_win(self):
        result_difference = self.m_score1 - self.m_score2

        if result_difference == 1:
            return "Advantage player1"
        elif result_difference == -1:
            return "Advantage player2"
        elif result_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_non_equal_scores(self):
        score = ""
        for points in range(1, 3):
            if points == 2:
                score += "-"
            temp_score = self.m_score2 if points == 2 else self.m_score1
            score += self.SCORE[temp_score]

        return score

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_equal_scores()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._get_advantage_or_win()
        else:
            return self._get_non_equal_scores()
