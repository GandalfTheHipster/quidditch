# team.py

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []  # Initialize an empty list of players
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0  # Total points for the season
        self.snitch_catch = False

    def add_player(self, player):
        self.players.append(player)

    def list_players(self):
        for player in self.players:
            print(player)