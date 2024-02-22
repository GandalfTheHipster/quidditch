# team.py

class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0  # Total points for the season
        self.snitch_catch = False  # Reset before each game in the loop
