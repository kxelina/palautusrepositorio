import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        nat = player_dict['nationality']
        if nat == 'FIN':
            players.append(player)

    print(f'Player from FIN')

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
