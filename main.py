# main.py

import random
import csv
from quidditch_game import simulate_quidditch_game
from schedule import generate_schedule
from team import Team  # Importing the Team class from team.py
from print_text import print_standings

# Setup
team_names = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
teams = [Team(name) for name in team_names]
schedule = generate_schedule(teams)

# Game results storage for CSV
game_details = []

# Simulation
for game in schedule:
    team1, team2 = game
    team1.snitch_catch = team2.snitch_catch = False  # Reset before each game
    result = simulate_quidditch_game(team1, team2)
    game_details.append(result)

# Writing to CSV
with open('quidditch_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Team 1', 'Team 2', 'Team 1 Points', 'Team 2 Points', 'Snitch Catch'])
    for game in game_details:
        writer.writerow([game['team1_name'], game['team2_name'], game['team1_points'], game['team2_points'], game['snitch_catch']])

# Display final standings
print_standings(teams)
