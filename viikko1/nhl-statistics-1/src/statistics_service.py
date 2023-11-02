from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def sort_by_points(player):
    return player.points

def sort_by_assits(player):
    return player.assists

def sort_by_goals(player):
    return player.goals

class StatisticsService:
    def __init__(self, reader = PlayerReader()):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort = SortBy.POINTS):

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=[sort_by_points, sort_by_goals, sort_by_assits][int(sort.value)-1]
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
