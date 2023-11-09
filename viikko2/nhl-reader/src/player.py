class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']

    def goals_and_assists(self):
        return f'{self.goals} + {self.assists} = {self.goals + self.assists}'

    def __str__(self):
        return f'{self.name.ljust(20)} {self.team.ljust(5)}{self.goals_and_assists()}'