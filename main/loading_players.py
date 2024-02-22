import csv
from player import Player
from team import Team

# Initialize a dictionary to hold team objects
teams = {}

# Function to load players from CSV and add them to teams
def load_players(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            team_name = row['team']
            name = row['name']
            position = row['position']
            skill_level = int(row['skill_level'])  # Assuming skill_level is a number

            # Create the player
            player = Player(team_name, name, position, skill_level)

            # Check if the team exists, and if not, create it
            if team_name not in teams:
                teams[team_name] = Team(team_name)
            
            # Add the player to the team
            teams[team_name].add_player(player)

# New function to list teams and their players
def list_teams():
    for team_name, team in teams.items():
        print(f"\n{team_name} Roster:")
        team.list_players()
