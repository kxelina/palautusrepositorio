import unittest
from statistics_service import StatisticsService
from player import Player

from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_players(self):
        search=self.stats.search("Kurri")
        self.assertEqual(str(search), 'Kurri EDM 37 + 53 = 90')
        search=self.stats.search("Hello")
        self.assertEqual(search, None)

    def test_team(self):
        team=self.stats.team("EDM")
        self.assertEqual(list(map(lambda x: x.name, team)), ["Semenko", "Kurri", "Gretzky"])

    def test_top_score(self):
        top= self.stats.top(1)
        self.assertEqual(str(top[0]), 'Gretzky EDM 35 + 89 = 124')

    def test_goals(self):
        goals=self.stats.top(1, SortBy.GOALS)
        self.assertEqual(str(goals[0]), 'Lemieux PIT 45 + 54 = 99')
                         
    def test_assit(self):
        assits=self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(str(assits[0]), 'Gretzky EDM 35 + 89 = 124')




